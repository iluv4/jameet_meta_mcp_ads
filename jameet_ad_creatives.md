# 자밋(Jameet) Meta 광고 소재 패키지

> 작성일: 2026-06-11
> 대상 광고 계정: `2062013064377322` (Jameet, KRW) / 비즈니스: Jameet (`2055716355052915`)

## ⚠️ 현재 차단 사항 (실행 전 확인)

| 항목 | 상태 | 조치 |
|---|---|---|
| Ads MCP 활성화 | ❌ 두 계정 모두 `is_ads_mcp_enabled: false` — Meta가 점진 롤아웃 중이라 모든 MCP 호출이 서버에서 거부됨 | 기다렸다가 재시도 (계정 설정으로 해결 불가) |
| 결제 수단 | ❌ Jameet 계정에 결제 수단 미등록 (`has_payment_method: false`) | 광고 관리자에서 결제 수단 등록 (생성은 가능하나 게재 불가) |
| 데이팅 광고 사전 승인 | ⚠️ Meta는 온라인 데이팅 서비스 광고에 **사전 서면 승인**을 요구함 | [Meta 데이팅 광고 정책](https://www.facebook.com/business/help/1100022406905185) 신청 필요. 미승인 시 소재가 반려됨 |
| 페이지 연결 | ⚠️ 현재 토큰으로 조회되는 페이지 0개 | 자밋 Facebook 페이지를 비즈니스에 연결하고 광고 권한 부여 |

## 제품 요약 (리서치 기반)

- **자밋**: 라이프스타일 기반 자만추(자연스러운 만남 추구) 미팅·소개팅 앱
- 슬로건: "오늘 만나는 사람이 인연이 될지도 모릅니다"
- 핵심 차별점:
  1. **오늘미팅** — 당일 바로 만나는 실시간 미팅
  2. **지인 동반 미팅** — 1:1부터 친구와 함께하는 그룹 미팅
  3. **검증 시스템** — 본인인증 + 학교·직장 서류/프로필 심사 통과 회원만 가입
  4. **지인차단** — 연락처 기반으로 아는 사람 노출 차단
  5. **후불제 소개팅** — 매칭 전 대표사진만 공개, 매칭 후 전체 프로필
- 링크:
  - 웹: https://www.jameet.co.kr/
  - App Store: https://apps.apple.com/kr/app/id6743886266
  - Google Play: https://play.google.com/store/apps/details?id=jameet2.lusoft.android

## 광고 소재 3종

### 소재 A — 즉시성 앵글 "오늘미팅"

| 필드 | 값 |
|---|---|
| 소재명 | `jameet_creative_A_today_meeting` |
| 본문 (message) | 소개팅 잡고 2주 기다리기, 지치지 않으셨나요? 자밋 '오늘미팅'에서는 오늘 바로 만날 수 있어요. 본인인증과 학교·직장 검증을 마친 회원들과 부담 없는 자연스러운 만남을 시작하세요. |
| 헤드라인 (headline) | 검증된 사람과, 오늘 바로 만나는 미팅 |
| 설명 (description) | 학교·직장 검증 기반 자만추 앱 |
| CTA | `INSTALL_MOBILE_APP` (앱 설치 캠페인) / 웹 랜딩이면 `LEARN_MORE` |
| 이미지 가이드 | 저녁 시간대 활기찬 거리/카페에서 휴대폰을 보며 미소 짓는 20~30대. "오늘미팅" 텍스트 오버레이. 1080×1080 (피드), 1080×1920 (스토리/릴스) |

### 소재 B — 부담 제거 앵글 "지인 동반 미팅"

| 필드 | 값 |
|---|---|
| 소재명 | `jameet_creative_B_group_meeting` |
| 본문 (message) | 1:1 소개팅은 부담스럽고, 자만추는 기회가 없고. 그래서 자밋엔 친구랑 같이 나가는 '지인 동반 미팅'이 있어요. 어색함은 반으로, 즐거움은 두 배로. 오늘 친구 한 명만 데려오세요. |
| 헤드라인 (headline) | 친구랑 같이 나가는 미팅, 자밋 |
| 설명 (description) | 지인 동반 그룹 미팅부터 1:1까지 |
| CTA | `INSTALL_MOBILE_APP` / `LEARN_MORE` |
| 이미지 가이드 | 2:2 그룹이 펍/보드게임 카페에서 웃는 장면. 친구 동반의 편안함 강조. 밝고 캐주얼한 톤 |

### 소재 C — 신뢰·안전 앵글 "검증 + 지인차단" (직장인 타겟)

| 필드 | 값 |
|---|---|
| 소재명 | `jameet_creative_C_verified_safe` |
| 본문 (message) | 프로필만 봐서는 알 수 없으니까. 자밋은 본인인증 + 서류·프로필 심사를 통과한 검증된 회원만 가입할 수 있어요. 연락처 기반 지인차단으로 아는 사람을 만날 걱정도 없죠. 바쁜 직장인을 위한 안전한 자만추. |
| 헤드라인 (headline) | 학교·직장 검증된 회원만 만나세요 |
| 설명 (description) | 지인차단으로 더 안전한 만남 |
| CTA | `INSTALL_MOBILE_APP` / `LEARN_MORE` |
| 이미지 가이드 | 깔끔한 오피스룩 인물 + 체크마크/인증 배지 그래픽. "서류 심사 통과 회원만" 텍스트 오버레이. 신뢰감 있는 차분한 톤 |

## Ads MCP 활성화 후 실행 플랜 (모두 PAUSED로 생성 → 검토 후 활성화)

1. **페이지 확인**: `ads_get_ad_account_pages(ad_account_id="2062013064377322")` → `page_id` 확보
2. **캠페인 생성** (CBO, 일 ₩20,000):
   ```json
   {
     "ad_account_id": "2062013064377322",
     "campaign_name": "자밋_앱설치_2026Q2",
     "objective": "OUTCOME_APP_PROMOTION",
     "buying_type": "AUCTION",
     "campaign_daily_budget": 20000,
     "special_ad_categories": "[]"
   }
   ```
   - 웹 트래픽 목적이면 `objective: "OUTCOME_TRAFFIC"` 으로 변경
3. **광고 세트 생성** (데이팅 정책상 성인 타겟 필수 — 연령 하드캡 적용):
   ```json
   {
     "ad_set_name": "자밋_KR_20-39",
     "billing_event": "IMPRESSIONS",
     "optimization_goal": "APP_INSTALLS",
     "targeting": "{\"geo_locations\":{\"countries\":[\"KR\"]},\"age_min\":20,\"age_max\":39,\"targeting_automation\":{\"advantage_audience\":0}}",
     "promoted_object": "{\"application_id\":\"<APP_ID>\",\"object_store_url\":\"https://play.google.com/store/apps/details?id=jameet2.lusoft.android\"}"
   }
   ```
4. **소재 3종 생성**: `ads_create_creative` — 위 표의 본문/헤드라인/설명/CTA + `image_url` (이미지 URL 직접 사용 가능, 사전 업로드 불필요)
5. **광고 3개 생성**: `ads_create_ad` — 각 소재를 `{"creative_id": "..."}` 로 연결
6. **미리보기**: `ads_get_ad_preview` (MOBILE_FEED_STANDARD / INSTAGRAM_STORY)
7. **사용자 최종 확인 후** `ads_activate_entity` 캠페인 → 광고 세트 → 광고 순서로 활성화
