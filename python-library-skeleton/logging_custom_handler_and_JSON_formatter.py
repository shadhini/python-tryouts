import logging
import json
# ----------------------------------------------------------------------------------------------------------------------
# FOLLOWING IS AN EXAMPLE OF A CUSTOM JSON LOGGING FORMATTER
# ----------------------------------------------------------------------------------------------------------------------

# This class defines a custom logging formatter that outputs each log record as a JSON string.
#   1. Builds a dictionary with standard fields:
#       timestamp, level, logger name, message, module, and function
#   2. If an exception exists (record.exc_info), it adds a formatted traceback.
#   3.cReturns json.dumps(log_data) so handlers write structured JSON instead of plain text.
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
        }

        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_data)


if __name__ == "__main__":
    # Example usage of the JsonFormatter
    logger = logging.getLogger("abc_library")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()  # or logging.FileHandler("app.log")
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)

    logger.info("Service started")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Computation failed")

