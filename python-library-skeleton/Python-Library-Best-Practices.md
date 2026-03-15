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

