from transformers import pipeline
from signals.scoring import determine_confidence_and_signal

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def analyze(asset: str, articles: list, financials: dict) -> str:
    combined_news = "\n".join(
        f"{a['title']}. {a.get('description', '')}" for a in articles
    )[:1000]

    financial_block = "\n".join(
        f"{k}: {v}" for k, v in financials.items() if v is not None
    )

    prompt = f"""
ASSET: {asset}

NEWS:
{combined_news}

FINANCIAL METRICS:
{financial_block}
"""

    summary = summarizer(
        prompt,
        max_length=220,
        min_length=80,
        do_sample=False
    )[0]["summary_text"]

    confidence, decision = determine_confidence_and_signal(summary)

    return f"""
📊 Market Research Update
Asset: {asset}

Summary:
{summary}

🧠 AI Confidence: {confidence}
📌 BUY OR NOT?: {decision}

⚠️ AI-assisted research, NOT financial advice.
"""
