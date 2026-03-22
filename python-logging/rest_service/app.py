from flask import Flask, request
import sys
from pathlib import Path
from routes import process_request

# Add the parent directory of the current file to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from logging_setup import setup_logging, get_logger

app = Flask(__name__)

# Setup logging once at application startup
setup_logging()

logger = get_logger('rest_service')

# Log all requests
@app.before_request
def log_request():
    logger.info(f"{request.method} {request.path} - {request.remote_addr}")

@app.after_request
def log_response(response):
    logger.info(f"Response: {response.status_code}")
    return response

# Error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    return {"error": "Internal server error"}, 500

if __name__ == '__main__':
    logger.info("Log Info @rest-service: Starting REST service")
    logger.debug("Log Debug @rest-service: Debugging REST service startup")
    logger.warning("Log Warning @rest-service: Rest service startup warning")
    app.run(debug=False)
    process_request(23)
    logger.error("Log Error @rest-service: Rest service startup errors")
