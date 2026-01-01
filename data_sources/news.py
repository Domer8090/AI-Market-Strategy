import requests
from config.settings import NEWS_API_KEY
from loguru import logger

def fetch_news(asset: str, limit: int = 5):
    """
    Pulls recent news articles for a given asset.
    This is intentionally shallow — raw data is later refined by the LLM.
    """
    if not NEWS_API_KEY:
        logger.warning("NEWS_API_KEY not set — skipping news fetch")
        return []

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": asset,
        "language": "en",
        "pageSize": limit,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    articles = response.json().get("articles", [])
    logger.info(f"Fetched {len(articles)} news articles for {asset}")
    return articles
