"""Blackship 일반 설정

민감한 정보는 넣지 않는다.
- 앱키/시크릿 : chest.py
- 복호화키 : chestkey.py

현재는 AliExpress만 사용한다.
나중에 Amazon 등 다른 쇼핑몰을 추가하면
아래처럼 같은 방식으로 설정만 늘리면 된다.
"""

# ==========================================================
# 공통 설정
# ==========================================================

SITE_BASE_URL = "https://blackship.kr"

# 기본 검색어
DEFAULT_KEYWORD = "keyboard"

# all / ko / en
BLACKSHIP_LANG = "all"

# 전체 상품 슬롯 수
BLACKSHIP_MAX_PRODUCT_SLOTS = 420

# 큐레이션 페이지 상품 수
BLACKSHIP_CURATION_PAGE_SIZE = 105


# ==========================================================
# AliExpress 설정
# ==========================================================

ALIEXPRESS_TRACKING_ID = ""
ALIEXPRESS_BASE_URL = "https://api-sg.aliexpress.com/sync"

ALIEXPRESS_PRODUCT_QUERY_METHOD = "aliexpress.affiliate.product.query"
ALIEXPRESS_HOT_PRODUCT_METHOD = "aliexpress.affiliate.hotproduct.query"

# 기본 정렬(빈 값이면 API 기본값)
ALIEXPRESS_SORT = ""

# 언어별 요청값
ALIEXPRESS_LANGUAGE_DEFAULTS = {
    "ko": {
        "target_currency": "KRW",
        "target_language": "KO",
        "ship_to_country": "KR",
    },
    "en": {
        "target_currency": "USD",
        "target_language": "EN",
        "ship_to_country": "US",
    },
}

# ==========================================================
# Amazon.com 설정
# ==========================================================


