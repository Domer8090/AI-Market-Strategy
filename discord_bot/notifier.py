import requests
from config.settings import DISCORD_WEBHOOK_URL

DISCLAIMER = "⚠️ This is AI-assisted research, NOT financial advice."

def send_to_discord(signal: dict):
    content = f"""
**📊 Market Research Update**
**Asset:** {signal['asset']}

{signal['analysis']}

🕒 {signal['timestamp']}
{DISCLAIMER}
"""

    payload = {"content": content}
    requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
