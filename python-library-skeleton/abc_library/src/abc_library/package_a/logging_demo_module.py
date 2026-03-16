import logging

# This creates a logger named "abc_library.logging_demo_module"
logger = logging.getLogger(__name__)

def some_function(item_id, data):
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.exception("Exception with traceback")

    # ✅ GOOD - String formatting only happens if message is logged
    logger.debug("Processing item %s with data %s", item_id, data)

    # ❌ BAD - String formatting happens even if debug is disabled
    logger.debug(f"Processing item {item_id} with data {data}")

