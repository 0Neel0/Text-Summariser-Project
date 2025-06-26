import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.TextSummarizer.logging import logger

logger.info("Welcome to our custom log")