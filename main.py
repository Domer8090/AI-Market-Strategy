from data_sources.news import fetch_news
from data_sources.financials import fetch_financials
from llm_analysis.analyzer import analyze
from discord_bot.notifier import send_to_discord

WATCHLIST = ["AAPL", "TSLA", "BTC"]

def run():
    for asset in WATCHLIST:
        news = fetch_news(asset)
        financials = fetch_financials(asset)
        report = analyze(asset, news, financials)
        send_to_discord(report)

if __name__ == "__main__":
    run()
