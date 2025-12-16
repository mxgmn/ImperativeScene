import logging
from functools import lru_cache
from colorlog import ColoredFormatter

@lru_cache
def get_logger():
    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()  # Logs to the console
        formatter = ColoredFormatter(
            #"%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "%(log_color)s%(message)s",
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'white',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)  # Set the log level
    return logger

my_logger = get_logger()

def info(s: str = "") -> None:
    my_logger.info(s)

def debug(s: str = "") -> None:
    my_logger.debug(s)

def warning(s: str = "") -> None:
    my_logger.warning(s)

def critical(s: str = "") -> None:
    my_logger.critical(s)
