# Python Logging Template
A production-ready Python logging configuration template.

## Logging Best Practices in Python

1. Do not duplicate configuration loading 
    - Load configuration once at application startup and pass it to components that need it.
    - Avoid loading configuration in multiple places (e.g., both in `main.py` and in `logging_config.py`).
      - This can cause
        - Race conditions
        - Handler duplication -- logs appearing multiple times
        - Performance overhead
2. Use a centralized logging configuration
3. Create logs directory automatically if it doesn't exist
4. Do not use f-strings in log messages; use %-style formatting (lazy formatting) instead for better performance
5. Add context using context filters or structured logging

### Performance Considerations

#### Use lazy formatting for performance:

```python name=your_library/performance.py
import logging

logger = logging.getLogger(__name__)

# ✅ GOOD - String formatting only happens if message is logged
logger.debug("Processing item %s with data %s", item_id, data)

# ❌ BAD - String formatting happens even if debug is disabled
logger.debug(f"Processing item {item_id} with data {data}")
```

#### Check log level only for expensive computations:
Python's `logging` checks the level before formatting, and using the `%s`-style arguments defers formatting until needed.
So no need to check `logger.isEnabledFor(logging.DEBUG)` for simple log statements.

Use `logger.isEnabledFor(logging.DEBUG)` only when preparing the log arguments is expensive:

```python
python
# cheap / lazy formatting (good)
logger.debug("Directory created: %s", dir_path)

# expensive computation (guard with check)
if logger.isEnabledFor(logging.DEBUG):
    details = expensive_computation()
    logger.debug("Details: %s", details)
```

### Key Principles

1. ✅ **DO**: Add `NullHandler` to your library's root logger
2. ✅ **DO**: Use `logging.getLogger(__name__)` in each module -- per module logger
3. ✅ **DO**: Use lazy formatting (`%s`, `%d`) instead of f-strings
4. ✅ **DO**: Let users configure logging in their application -- use a `NullHandler`
5. ✅ **DO**: Document your logging behavior and provide an example app config in the `README`
6. ❌ **DON'T**: Call `logging.basicConfig()` in library code -- libraries should never configure logging handlers by default
7. ❌ **DON'T**: Add any handlers except `NullHandler`
8. ❌ **DON'T**: Set logging levels in library code
9. ❌ **DON'T**: Configure logging output format

## Project structure

```text
python-logging/
├── README.md                         # Documentation
├── requirements.txt                  # Dependencies
├── .gitignore                        # Ignore logs/
├── logging_setup.py                  # Single source of truth
├── structlog_setup.py                # For structured logging with context
├── config/
│   ├── logging_config.ini           
│   ├── logging_config_dev.ini       # Development config
│   └── logging_config_prod.ini      # Production config
├── logs/                            
│   ├── .gitkeep
│   └── README.md                    
├── my_library/
│   ├── __init__.py                  
│   ├── utils.py                     
│   └── sub_library_package/
│       └── __init__.py
├── my_package/
│   ├── __init__.py                  
│   └── module.py                    
├── rest_service/
│   ├── __init__.py                 
│   ├── app.py                       
│   └── routes.py                  
└── scripts/
    ├── __init__.py                  
    └── data_processor.py            

```

## Quick Start

1. Application/Script Entry Points (where `if __name__ == '__main__'` or app startup):
   - Call `setup_logging()` once at the very beginning 
   - Examples: `rest_service/app.py`, `scripts/data_processor.py`

2. Libraries and Modules (imported by other code):
   - Just use `logging.getLogger(__name__)` or `logging.getLogger('my_library')`
   - Add NullHandler() to prevent warnings
   - DO NOT call `setup_logging()`
   - Examples: `my_library/`, `my_package/`, utility modules

3. Regular Modules (routes.py, utils.py, module.py):
   - Just use `logging.getLogger(__name__)` or specific name 
   - No imports from `logging_setup` needed

### Basic Setup
```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from logging_setup import setup_logging, get_logger

# Call once at application startup
setup_logging()

# In your modules
logger = get_logger(__name__)
logger.info("Application started")
```

### Structured Logging with Context
```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from structlog_setup import setup_structlog, get_logger

# Setup structlog
setup_structlog()

logger = get_logger('rest_service')
```

## Test Run

```bash
# Test the script
python scripts/data_processor.py

# Test the Flask app
python rest_service/app.py
```

## About logging configuration: `logging_config.ini`

### [loggers] `propagate` field 
```ini
[loggers]
keys=root,scripts

# Root logger - catches everything not explicitly configured
[logger_root]
level=INFO
handlers=consoleHandler,errorFileHandler

# Scripts logger
[logger_scripts]
level=INFO
handlers=consoleHandler,fileHandler
qualname=scripts
propagate=0
```
controls whether log messages are passed to handlers of ancestor (parent) loggers
- `propagate=0` (or `False`): Stops propagation - messages are only handled by this logger's handlers
- `propagate=1` (or `True`, default): Messages propagate up to parent loggers' handlers

In this config, 
- `propagate=0` for the `scripts` logger means 
  - log messages will only go to `consoleHandler` and `fileHandler`, and 
  - won't be passed to the root logger's handlers (`consoleHandler` and `errorFileHandler`)
- this prevents duplicate logging

### [handlers.RotatingFileHandler] `args` field
    
```ini
[handlers]
keys=fileHandler

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=detailedFormatter
args=('logs/app.log', 'a', 10485760, 5)
```

1. **`'logs/app.log'`** - The log file path
2. **`'a'`** - File mode (append mode)
3. **`10485760`** - Maximum file size in bytes (10 MB = 10 * 1024 * 1024)
   - when the log file reaches 10 MB, it will be rotated: 
     - the current file is renamed (e.g., `app.log.1`), and a new `app.log` is created
4. **`5`** - Number of backup files to keep
   - up to 5 backup files (`app.log.1` through `app.log.5`) are kept before the oldest is deleted


