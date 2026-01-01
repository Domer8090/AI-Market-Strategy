import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

MODEL_NAME = "gpt-3.5-turbo" # cost-effective research model
