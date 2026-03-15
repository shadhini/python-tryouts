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

