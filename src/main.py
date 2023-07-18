from movies_scraper import run
from src.config import config


def main() -> None:
    config()
    run()


if __name__ == "__main__":
    main()
    