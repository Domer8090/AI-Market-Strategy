from datetime import datetime

def build_signal(asset: str, analysis: str) -> dict:
    """
    Structures LLM output for downstream delivery.
    No numerical prediction or trading instruction is generated.
    """
    return {
        "asset": asset,
        "analysis": analysis,
        "timestamp": datetime.utcnow().isoformat()
    }
