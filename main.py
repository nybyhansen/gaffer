import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the gaffer entry point."""
    logging.basicConfig(level=logging.INFO)
    logger.info("Hello from gaffer!")


if __name__ == "__main__":
    main()
