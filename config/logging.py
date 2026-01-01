from loguru import logger

logger.add(
    "logs/system.log",
    rotation="5 MB",
    level="INFO",
    format="{time} | {level} | {message}"
)
