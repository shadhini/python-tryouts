import logging

logger = logging.getLogger('my_library.utils')

def my_library_utils_method1(data=0):
    logger.info("Info Log @my_library_utils_method1: Inside my_library_utils_method1")
    logger.debug("Debug Log @my_library_utils_method1: Processing data: %s", data)
    logger.warning("Warning Log @my_library_utils_method1: This is a warning message -- upcoming zero division")
    try:
        result = data / 0
        logger.info("Info Log @my_library_utils_method1: Data processed successfully")
        return result
    except Exception as e:
        logger.error("Error Log @my_library_utils_method1: Failed to process data: %s", e, exc_info=True)
        raise
