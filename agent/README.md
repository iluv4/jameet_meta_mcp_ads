# 자밋 광고 업로드 에이전트

`creatives.json`에 정의된 소재를 Meta Marketing API로 일괄 업로드합니다.
Ads MCP 롤아웃과 무관하게 동작합니다 (Graph API 직접 호출).

> ⚠️ Claude 세션 컨테이너에서는 네트워크 정책상 graph.facebook.com 접근이
> 차단되므로, 이 스크립트는 **본인 PC에서** 실행해야 합니다.

## 1. 액세스 토큰 발급 (최초 1회)

권장: 비즈니스 설정의 시스템 사용자 토큰 (만료 없음)

1. [business.facebook.com](https://business.facebook.com) → 비즈니스 설정 → 사용자 → **시스템 사용자** → 추가
2. 생성한 시스템 사용자에 **자산 할당**: 광고 계정(`2062013064377322`, 관리 권한) + 자밋 페이지(콘텐츠 게시 권한)
3. **토큰 생성** → 권한 체크: `ads_management`, `pages_read_engagement`, `business_management`
4. 토큰을 복사해 `.env`에 저장

간단 테스트용은 [Graph API 탐색기](https://developers.facebook.com/tools/explorer)에서
같은 권한의 사용자 토큰을 발급해도 됩니다 (1~2시간 만료 주의).

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

- [ ] 광고 계정에 결제 수단 등록
- [ ] Meta 데이팅 광고 사전 승인 획득 (미승인 시 심사 반려)
- [ ] `creatives.json`의 `jameet_D_host_privacy`에 브랜드 소재 이미지 URL 입력
- [ ] `--dry-run`으로 카피/타겟팅 최종 확인

## 소재 수정

`creatives.json`만 고치면 됩니다. `image_url`이 비어 있는 소재는
건너뛰고 경고만 출력합니다.
