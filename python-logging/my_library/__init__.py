import logging

# For libraries: just get a logger, don't configure
# Let the application that uses this library handle configuration
logger = logging.getLogger('my_library')

# Add NullHandler to prevent "No handler" warnings if app doesn't configure logging
logger.addHandler(logging.NullHandler())
