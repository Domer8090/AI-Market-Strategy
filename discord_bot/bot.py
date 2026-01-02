import discord
import os
from discord.ext import commands
from data_sources.news import fetch_news
from data_sources.financials import fetch_financials
from llm_analysis.analyzer import analyze

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def research(ctx, symbol: str):
    symbol = symbol.upper()

    await ctx.send(f"🔍 Running research for {symbol}...")

    news = fetch_news(symbol)
    financials = fetch_financials(symbol)
    report = analyze(symbol, news, financials)

    await ctx.send(report)

bot.run(os.environ["DISCORD_BOT_TOKEN"])
