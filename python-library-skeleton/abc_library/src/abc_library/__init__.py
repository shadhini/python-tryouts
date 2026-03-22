"""
ABC Library - A sample Python library
"""
from .package_a.core import A1, A2
from .package_b.utils import utility_function_a, utility_function_b
import logging

# Setting up logging for the library

# Create a logger for your library
logger = logging.getLogger(__name__)

# Add NullHandler to prevent "No handler found" warnings
logger.addHandler(logging.NullHandler())


# Optionally expose a convenience function for users
def setup_logging(level=logging.WARNING):
    """
    Convenience function for library users to enable logging.

    Args:
        level: Logging level (default: WARNING)

    Example:
        >>> import abc_library
        >>> abc_library.setup_logging(logging.DEBUG)
    """
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)


__version__ = "1.0.0"
__author__ = "Shadhini Jayatilake"
__email__ = "shadhini.jayatilake@gmail.com"

__all__ = ['A1', 'A2', 'utility_function_a', 'utility_function_b']
