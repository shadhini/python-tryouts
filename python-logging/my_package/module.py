import logging

logger = logging.getLogger('my_package.module')


class MyClass:
    def __init__(self):
        logger.debug("my_package: MyClass initialized")

    def do_something(self):
        logger.info("Doing something")

    def my_package_module_method1(data=0):
        logger.info("Info Log @my_package_module_method1: Inside my_package_module_method1")
        logger.debug("Debug Log @my_package_module_method1: Processing data : %s", data)
        logger.warning("Warning Log @my_package_module_method1: This is a warning message -- upcoming zero division")
        try:
            result = data / 0
            logger.info("Info Log @my_package_module_method1: Data processed successfully")
            return result
        except Exception as e:
            logger.error(f"Error Log @my_package_module_method1: Failed to process data: {e}", exc_info=True)
            raise

