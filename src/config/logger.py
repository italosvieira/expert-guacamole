import logging
import os


def config_logger() -> None:
    log_level = "INFO" if os.getenv("PYTHON_ENV") == "production" else "DEBUG"

    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(levelname)s] - %(message)s", "%Y-%m-%dT%H:%M:%S%z"
        )
    )

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(handler)
