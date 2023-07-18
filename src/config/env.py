import logging
import os
import sys


def validate_env_variables() -> None:
    if os.getenv("PYTHON_ENV") is None:
        logging.error("PYTHON_ENV can't be None. Exiting with code 1.")
        sys.exit(1)


def config_env() -> None:
    if os.getenv("PYTHON_ENV") != "production":
        from dotenv import load_dotenv

        load_dotenv()

    validate_env_variables()
