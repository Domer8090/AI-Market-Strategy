from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from loguru import logger

MODEL_NAME = "facebook/bart-large-cnn"

def load_summarizer():
    logger.info(f"Loading summarization model: {MODEL_NAME} (this may take a few minutes on first run)...")
    summarizer = pipeline("summarization", model=MODEL_NAME)
    logger.info("Model loaded successfully.")
    return summarizer

summarizer = load_summarizer()

def analyze(asset: str, articles: list) -> str:
    combined_text = "\n".join(
        f"{a['title']}. {a.get('description', '')}" for a in articles
    )
    combined_text = combined_text[:1000]

    try:
        summary_result = summarizer(combined_text, max_length=150, min_length=40, do_sample=False)
        summary_text = summary_result[0]['summary_text']

        analysis = (
            f"Summary:\n{summary_text}\n\n"
            "Note: Local model summary — no confidence scores.\n"
            "This is research assistance, not financial advice."
        )

        logger.info(f"Analysis completed for {asset}")
        return analysis
    except Exception as e:
        logger.error(f"Summarization error: {e}")
        return "⚠️ Error: Failed to generate summary."
