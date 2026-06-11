# 자밋 광고 업로드 에이전트

`creatives.json`에 정의된 소재를 Meta Marketing API로 일괄 업로드합니다.
Ads MCP 롤아웃과 무관하게 동작합니다 (Graph API 직접 호출).

> ⚠️ Claude 세션 컨테이너에서는 네트워크 정책상 graph.facebook.com 접근이
> 차단되므로, 이 스크립트는 **본인 PC에서** 실행해야 합니다.

## 1. 액세스 토큰 발급 (최초 1회)

집행 계정이 **개인 광고 계정**(`27049951394664152`)이므로 사용자 토큰이 가장 간단합니다:

1. [Graph API 탐색기](https://developers.facebook.com/tools/explorer) 접속 → 본인 앱 선택 (없으면 developers.facebook.com에서 비즈니스 유형 앱 1개 생성)
2. 권한 추가: `ads_management`, `pages_read_engagement`, `pages_show_list`
3. **Generate Access Token** → 복사해 `.env`에 저장
4. 탐색기 토큰은 1~2시간 만료이므로, 계속 쓰려면 [액세스 토큰 디버거](https://developers.facebook.com/tools/debug/accesstoken/)에서 "장기 실행 토큰으로 교환" (60일)

비즈니스 계정(Jameet, `2062013064377322`)으로 전환할 경우에는 비즈니스 설정 →
시스템 사용자 토큰(만료 없음)을 권장하며, 시스템 사용자에 광고 계정 + 페이지
자산 할당이 필요합니다.

## 2. 설정

```bash
cd agent
cp .env.example .env   # 토큰/계정/페이지 ID 입력
```

`PAGE_ID`는 facebook.com/자밋페이지 → 정보 → 페이지 투명성에서 확인.

## 3. 실행 (Python 3.8+, 외부 패키지 불필요)

```bash
python upload_ads.py --dry-run   # 생성될 내용 미리보기
python upload_ads.py             # PAUSED 상태로 캠페인/세트/소재/광고 생성
python upload_ads.py --activate  # 생성 + 즉시 활성화 (과금 시작!)
```

## 4. 게재 전 체크리스트

- [x] 광고 계정에 결제 수단 등록 (개인 계정 `27049951394664152` 사용)
- [x] Meta 데이팅 광고 사전 승인 획득 (2026-06-11 승인 완료)
- [ ] `creatives.json`의 `jameet_D_host_privacy`에 브랜드 소재 이미지 URL 입력
- [ ] `--dry-run`으로 카피/타겟팅 최종 확인

## 소재 수정

`creatives.json`만 고치면 됩니다. `image_url`이 비어 있는 소재는
건너뛰고 경고만 출력합니다.
