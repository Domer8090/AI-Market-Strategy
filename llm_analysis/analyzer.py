from transformers import pipeline
from loguru import logger
from datetime import datetime

MODEL_NAME = "facebook/bart-large-cnn"

try:
    summarizer = pipeline("summarization", model=MODEL_NAME)
except Exception as e:
    logger.error(f"Failed to load summarization model: {e}")
    summarizer = None


def determine_confidence_and_signal(summary: str):
    """
    Heuristic to assign confidence and buy/sell signal based on keywords.
    This is a simple rule-based system for demonstration only.
    """

    bullish_keywords = ["buy", "bullish", "outperform", "upgrade", "strong", "growth", "positive", "surge", "beat"]
    bearish_keywords = ["sell", "bearish", "downgrade", "weak", "decline", "risk", "drop", "miss", "concern", "fall"]

    summary_lower = summary.lower()

    bullish_score = sum(word in summary_lower for word in bullish_keywords)
    bearish_score = sum(word in summary_lower for word in bearish_keywords)

    # Confidence heuristics based on keyword count
    if bullish_score + bearish_score >= 3:
        confidence = "High"
    elif bullish_score + bearish_score == 2:
        confidence = "Medium"
    else:
        confidence = "Low"

    # Buy or Not decision (very simplistic)
    if bullish_score > bearish_score:
        decision = "BUY"
    elif bearish_score > bullish_score:
        decision = "NOT BUY"
    else:
        decision = "NO CLEAR SIGNAL"

    return confidence, decision


def analyze(asset: str, articles: list) -> str:
    """
    Local LLM-based research analysis with heuristic confidence and buy/not buy signal.
    """

    if summarizer is None:
        logger.error("Summarizer pipeline is not initialized.")
        return "⚠️ Error: Summarization model not loaded."

    combined_text = "\n".join(
        f"{a['title']}. {a.get('description', '')}" for a in articles
    )
    combined_text = combined_text[:1000]  # truncate if needed

    try:
        summary_result = summarizer(combined_text, max_length=150, min_length=40, do_sample=False)
        summary_text = summary_result[0]['summary_text']

        confidence, decision = determine_confidence_and_signal(summary_text)

        analysis = (
            f"Asset: {asset}\n\n"
            f"Summary:\n{summary_text}\n\n"
            f"AI Confidence Level: {confidence}\n"
            f"Preliminary Trading Signal: {decision}\n\n"
            f"Note: Local model summary — heuristic confidence and signals.\n"
            f"This is research assistance, not financial advice.\n\n"
            f"🕒 {datetime.utcnow().isoformat()}\n"
            f"⚠️ This is AI-assisted research, NOT financial advice."
        )

        logger.info(f"Local LLM analysis completed for {asset} with confidence {confidence} and decision {decision}")
        return analysis

    except Exception as e:
        logger.error(f"Error during summarization: {e}")
        return "⚠️ Error: Failed to generate summary."
