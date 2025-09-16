import sys
from loguru import logger

def setup_logging(app_name: str):
    logger.remove()
    logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                                  "<level>{level: <8}</level> | "
                                  f"{app_name} | "
                                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                                  "<level>{message}</level>")
    return logger
