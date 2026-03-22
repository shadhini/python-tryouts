import sys
from pathlib import Path

# Add the parent directory of the current file to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from logging_setup import setup_logging, get_logger

# Setup logging once at script startup
setup_logging()

logger = get_logger('scripts.data_processor')

def main():
    logger.info("Info Log: @script_data_processor: Starting data processor script")
    logger.debug("Debug Log: @script_data_processor: Starting data processor script")
    logger.warning("Warning Log: @script_data_processor: Starting data processor script")
    logger.error("Error Log: @script_data_processor: Starting data processor script")

    try:
        # Your script logic
        logger.debug("Debug information here")
        a = 1 / 0
        logger.info("Processing completed")
    except Exception as e:
        logger.error("Error Log: @script_data_processor: Script failed: %s", e, exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
