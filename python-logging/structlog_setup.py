import logging
import structlog
from pathlib import Path


def setup_structlog():
    """
    Configure structlog for structured logging with context.
    This is a production-ready configuration.
    """

    # Ensure logs directory exists
    log_dir = Path(__file__).parent / 'logs'
    log_dir.mkdir(exist_ok=True)

    # Configure structlog
    structlog.configure(
        processors=[
            # Add log level to event dict
            structlog.stdlib.add_log_level,
            # Add logger name
            structlog.stdlib.add_logger_name,
            # Add timestamp
            structlog.processors.TimeStamper(fmt="iso"),
            # Add stack info for exceptions
            structlog.processors.StackInfoRenderer(),
            # Format exceptions
            structlog.processors.format_exc_info,
            # Render to JSON for file output
            structlog.processors.JSONRenderer()
        ],
        # Use standard library logging
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging as backend
    logging.basicConfig(
        format="%(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(log_dir / 'structlog_app.log'),
            logging.StreamHandler()
        ]
    )


def get_logger(name):
    """Get a structlog logger."""
    return structlog.get_logger(name)

# -------------------------------------------------------------------------
# Example usage: Updated rest_service/app.py using structlog
# -------------------------------------------------------------------------

# from flask import Flask, request, g
# import sys
# from pathlib import Path
# import uuid
#
# sys.path.insert(0, str(Path(__file__).parent.parent))
#
# from structlog_setup import setup_structlog, get_logger
#
# app = Flask(__name__)
#
# # Setup structlog
# setup_structlog()
#
# logger = get_logger('rest_service')
#
#
# @app.before_request
# def setup_context():
#     """Set up context binding for the request."""
#     g.request_id = str(uuid.uuid4())
#
#     # Bind context to logger - it will be included in ALL subsequent logs
#     g.log = logger.bind(
#         request_id=g.request_id,
#         method=request.method,
#         path=request.path,
#         remote_addr=request.remote_addr,
#         user_agent=request.headers.get('User-Agent', 'unknown')
#     )
#
#     g.log.info("request_received")
#
#
# @app.route('/api/test')
# def test():
#     """Example endpoint."""
#     # Context is automatically included
#     g.log.info("processing_test_request", endpoint="test")
#     g.log.debug("test_details", some_data="example")
#
#     return {"message": "success", "request_id": g.request_id}
#
#
# @app.route('/api/users/<user_id>')
# def get_user(user_id):
#     """Example with additional context."""
#     # Add more context for this specific operation
#     user_log = g.log.bind(user_id=user_id, operation="get_user")
#     user_log.info("fetching_user")
#
#     # Simulate processing
#     user_log.debug("user_lookup", database="postgres")
#
#     return {"user_id": user_id, "request_id": g.request_id}
#
#
# @app.after_request
# def log_response(response):
#     """Log response."""
#     g.log.info(
#         "request_completed",
#         status_code=response.status_code,
#         content_length=response.content_length
#     )
#     return response
#
#
# @app.errorhandler(Exception)
# def handle_exception(e):
#     """Handle exceptions with context."""
#     g.log.error(
#         "unhandled_exception",
#         error_type=type(e).__name__,
#         error_message=str(e),
#         exc_info=True
#     )
#     return {"error": "Internal server error", "request_id": g.request_id}, 500
#
#
# if __name__ == '__main__':
#     logger.info("service_starting", port=5000, environment="development")
#     app.run(debug=False, port=5000)

# -------------------------------------------------------------------------
# Example Log Output: With structlog
# -------------------------------------------------------------------------

# {
#   "event": "processing_test_request",
#   "level": "info",
#   "logger": "rest_service",
#   "timestamp": "2026-03-21T10:30:45.123456Z",
#   "request_id": "abc-123-def-456",
#   "method": "GET",
#   "path": "/api/test",
#   "remote_addr": "192.168.1.100",
#   "endpoint": "test"
# }
