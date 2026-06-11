#!/usr/bin/env python3
"""자밋 Meta 광고 자동 업로드 에이전트.

creatives.json의 소재 정의를 읽어 Meta Marketing API로
캠페인 → 광고 세트 → 소재 → 광고를 일괄 생성한다 (기본 PAUSED).

사용법:
    python upload_ads.py --dry-run        # 호출 없이 생성될 내용만 출력
    python upload_ads.py                  # PAUSED 상태로 전체 생성
    python upload_ads.py --activate       # 생성 후 즉시 활성화 (과금 시작 주의)

필요 환경변수(.env 또는 셸 export):
    META_ACCESS_TOKEN  ads_management 권한의 액세스 토큰
    AD_ACCOUNT_ID      숫자만 (예: 2062013064377322)
    PAGE_ID            소재를 게시할 Facebook 페이지 ID
"""

import argparse
import base64
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error

GRAPH = "https://graph.facebook.com"
API_VERSION = os.environ.get("GRAPH_API_VERSION", "v23.0")


def load_env(path=".env"):
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def api(method, path, payload=None, token=None):
    url = f"{GRAPH}/{API_VERSION}/{path}"
    data = dict(payload or {})
    data["access_token"] = token
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=body if method == "POST" else None,
                                 method=method)
    if method == "GET":
        req = urllib.request.Request(f"{url}?{urllib.parse.urlencode(data)}")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise SystemExit(f"[Meta API 오류] {method} {path}\n{detail}")


def fetch_image_b64(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return base64.b64encode(r.read()).decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--activate", action="store_true")
    parser.add_argument("--config", default=os.path.join(
        os.path.dirname(__file__), "creatives.json"))
    args = parser.parse_args()

    load_env(os.path.join(os.path.dirname(__file__), ".env"))
    token = os.environ.get("META_ACCESS_TOKEN")
    account = os.environ.get("AD_ACCOUNT_ID")
    page_id = os.environ.get("PAGE_ID")
    if not args.dry_run and not all([token, account, page_id]):
        raise SystemExit("META_ACCESS_TOKEN / AD_ACCOUNT_ID / PAGE_ID 를 설정하세요 (.env 참고)")

    cfg = json.load(open(args.config, encoding="utf-8"))
    camp, adset, creatives = cfg["campaign"], cfg["adset"], cfg["creatives"]
    status = "ACTIVE" if args.activate else "PAUSED"

    print(f"캠페인 1개 / 광고 세트 1개 / 소재 {len(creatives)}개 → 상태 {status}")
    if args.dry_run:
        print(json.dumps(cfg, ensure_ascii=False, indent=2))
        return

    me = api("GET", "me", {"fields": "id,name"}, token)
    print(f"토큰 확인: {me.get('name')} ({me.get('id')})")

    campaign = api("POST", f"act_{account}/campaigns", {
        "name": camp["name"],
        "objective": camp["objective"],
        "status": status,
        "daily_budget": camp["daily_budget"],
        "special_ad_categories": "[]",
    }, token)
    print(f"캠페인 생성: {campaign['id']}")

    adset_res = api("POST", f"act_{account}/adsets", {
        "name": adset["name"],
        "campaign_id": campaign["id"],
        "billing_event": "IMPRESSIONS",
        "optimization_goal": adset["optimization_goal"],
        "targeting": json.dumps(adset["targeting"], ensure_ascii=False),
        "status": status,
    }, token)
    print(f"광고 세트 생성: {adset_res['id']}")

    for c in creatives:
        link_data = {
            "link": c["link"],
            "message": c["message"],
            "name": c["headline"],
            "description": c["description"],
            "call_to_action": {"type": c["cta"], "value": {"link": c["link"]}},
        }
        if c.get("image_url"):
            img = api("POST", f"act_{account}/adimages",
                      {"bytes": fetch_image_b64(c["image_url"])}, token)
            link_data["image_hash"] = next(iter(img["images"].values()))["hash"]
        else:
            print(f"  ⚠ {c['name']}: image_url 없음 → 건너뜀 (앱 화면 수급 후 추가)")
            continue

        creative = api("POST", f"act_{account}/adcreatives", {
            "name": c["name"],
            "object_story_spec": json.dumps(
                {"page_id": page_id, "link_data": link_data}, ensure_ascii=False),
        }, token)
        ad = api("POST", f"act_{account}/ads", {
            "name": c["name"],
            "adset_id": adset_res["id"],
            "creative": json.dumps({"creative_id": creative["id"]}),
            "status": status,
        }, token)
        print(f"광고 생성: {c['name']} → ad {ad['id']} (creative {creative['id']})")

    print("\n완료. Ads Manager에서 검토하세요:"
          f" https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={account}")
    if not args.activate:
        print("모두 PAUSED 상태입니다. 검토 후 활성화하세요.")
    print("주의: 데이팅 광고는 Meta 사전 승인 필요 / 결제 수단 등록 필수.")


if __name__ == "__main__":
    main()
