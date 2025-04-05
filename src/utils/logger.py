# utils/logger.py

import logging

def setup_logger():
    logger = logging.getLogger("TestLogger")
    handler = logging.FileHandler("logs/test_log.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()
