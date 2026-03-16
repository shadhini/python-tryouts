# Python Library Best Practices

## Project Structure

```text
my_library/
├── src/
│   └── my_library/             # Actual package source code
│       ├── __init__.py         # Makes the directory a package
│       ├── core.py
│       └── utils.py
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/                       # Documentation (Sphinx or MkDocs)
│   └── index.md
├── .github/                    # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── LICENSE
├── pyproject.toml              # Build system & metadata (The heart of the project)
├── README.md
└── setup.cfg                   # Optional (if not using pyproject.toml fully)
```


### The `src/` Layout

Industry experts prefer putting code in a `src/` subdirectory rather than the root.

* **Forces Installation:** It ensures that when you run tests, you are testing the **installed** version of your library, 
not just the local files. This catches "missing file" bugs before you ship.
* **Cleaner Root:** Keeps your root directory uncluttered from compiled `.pyc` files and build artifacts.

### `pyproject.toml`

The days of `setup.py` are mostly behind us (though it still works). 

`pyproject.toml` is the modern, unified way to define:
* Build requirements (Build-backend like Flit, Hatch, or PDM).
* Project metadata (Version, author, dependencies).
* Tool configuration (Black, Ruff, Mypy).

                               |
### `__init__.py`

**`__init__.py`**: Exposes the public API. It's best to keep this slim.  

### Automated Quality Control

A project isn't "industry standard" without a way to enforce quality. 

Usually, this involves a `.pre-commit-config.yaml` file to automate:
* **Linting:** Ruff or Flake8.
* **Formatting:** Black.
* **Type Checking:** Mypy.

## Logging

### Performance Considerations

Use lazy formatting for performance:

```python name=your_library/performance.py
import logging

logger = logging.getLogger(__name__)

# ✅ GOOD - String formatting only happens if message is logged
logger.debug("Processing item %s with data %s", item_id, data)

# ❌ BAD - String formatting happens even if debug is disabled
logger.debug(f"Processing item {item_id} with data {data}")
```

### Key Principles

1. ✅ **DO**: Add `NullHandler` to your library's root logger
2. ✅ **DO**: Use `logging.getLogger(__name__)` in each module -- per module logger
3. ✅ **DO**: Use lazy formatting (`%s`, `%d`) instead of f-strings
4. ✅ **DO**: Let users configure logging in their application -- use a `NullHandler`
5. ✅ **DO**: Document your logging behavior and provide an example app config in the `README`
5. ❌ **DON'T**: Call `logging.basicConfig()` in library code -- libraries should never configure logging handlers by default
6. ❌ **DON'T**: Add any handlers except `NullHandler`
7. ❌ **DON'T**: Set logging levels in library code
8. ❌ **DON'T**: Configure logging output format

