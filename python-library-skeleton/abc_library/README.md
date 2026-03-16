# ABC Library - Sample Python Library

A sample Python library that demonstrates a typical structure, features, installation, and usage. 
This library is designed to be a starting point for building your own Python package.

## Features

- Feature A
- Feature B
- Feature C

## Installation

### From source
```bash
pip install -e .
```

### For development
```bash
pip install -e ".[dev]"
```

## Usage

```python
from abc_library.hec_hms import HMSModelRunner
from abc_library.utils import validate_run_name

# Validate run name
if validate_run_name("my_run_2024"):
    print("Valid run name")

# Run HEC-HMS model
runner = HMSModelRunner(
    model_dir="/path/to/model",
    hms_home="/opt/hec-hms"
)
runner.prepare_run()
runner.execute()
```

## Modules

- `abc_library.hec_hms` - Core HEC-HMS automation
- `abc_library.utils` - Utility functions
- `abc_library.validators` - Input validation
- `abc_library.config` - Configuration management

## License

MIT License

# Logging

By default, this library uses a `NullHandler` and produces no output.

## Enable Logging

### Option 1: Use the convenience function
```python
import logging
import abc_library

abc_library.setup_logging(logging.DEBUG)
```

### Option 2: Configure manually
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Now abc_library logs will appear
import abc_library
```

### Option 3: Configure specific library logger
```python
import logging

logger = logging.getLogger('abc_library')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger.addHandler(handler)
```
