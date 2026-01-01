from data_sources.news import fetch_news
from llm_analysis.analyzer import analyze
from signals.research_signal import build_signal
from discord_bot.notifier import send_to_discord
from llm_analysis.analyzer import analyze

ASSETS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "NVDA", "AMD", "TSM", "INTC",
    "TSLA", "F", "GM",
    "JPM", "BAC", "GS",
    "KO", "PEP", "MCD",
    "WMT", "COST",
    "NFLX", "DIS",
    "XOM", "CVX",
    "PLTR", "SNOW", "CRM",
    "SPY", "QQQ",
    "BTC", "ETH"
]

def run():
    for asset in ASSETS:
        articles = fetch_news(asset)
        if not articles:
            continue

        analysis = analyze(asset, articles)
        signal = build_signal(asset, analysis)
        send_to_discord(signal)

if __name__ == "__main__":
    run()
