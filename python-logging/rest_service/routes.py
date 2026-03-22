import logging

logger = logging.getLogger('rest_service.routes')

def process_request(data=0):
    logger.debug(f"Debug Log @routes:process_request:Processing request with data: {data}")
    # Your logic here
    logger.info("Info Log @routes:process_request: Request processed successfully")
    logger.debug("Debug Log @routes:process_request: Finished processing request")
    logger.warning("Warn Log @routes:process_request: Finished processing request")
    logger.error("Error Log @routes:process_request: Finished processing request")
