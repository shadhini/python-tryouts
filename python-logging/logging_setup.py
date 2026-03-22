import logging
import logging.config
from pathlib import Path

_logging_configured = False

def ensure_log_directory():
    """Ensure the logs directory exists."""
    log_dir = Path(__file__).parent / 'logs'
    log_dir.mkdir(exist_ok=True)
    return log_dir


def setup_logging(config_file='config/logging_config.ini', default_level=logging.INFO):
    """
    Setup logging configuration.
    Should be called once at application startup.

    Args:
        config_file: Path to logging config file
        default_level: Default logging level if config file not found
    """

    global _logging_configured

    if _logging_configured:
        return

    # Ensure logs directory exists BEFORE loading config
    ensure_log_directory()

    config_path = Path(__file__).parent / config_file

    if config_path.exists():
        try:
            logging.config.fileConfig(
                config_path,
                disable_existing_loggers=False
            )
            _logging_configured = True
            logging.getLogger(__name__).info("Logging configured from %s", config_path)
        except Exception as e:
            logging.basicConfig(level=default_level)
            logging.getLogger(__name__).error("Failed to load logging config: %s", e)
    else:
        # Fallback to basic config
        logging.basicConfig(
            level=default_level,
            format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
        )
        logging.getLogger(__name__).warning("Config file not found: %s. Using basic config.", config_path)


def get_logger(name):
    """Get a logger instance with the given name."""
    return logging.getLogger(name)
