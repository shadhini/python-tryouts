# Pipfile Syntax

## `[packages]`
define your project's dependencies
- for a local library, the notation dictates how Pipenv handles the source code—whether it "snapshots" it or links to it.

### 1. The Local Library Notation
To include a library located on your Debian system (or inside your Docker build context):

```toml
[packages]
my_library = {path = "./my_local_lib", editable = true}
```

* **`path`**: The relative or absolute path to the directory containing your `pyproject.toml` or `setup.py`.
* **`editable = true`**: for your development environment so you don't have to run `pipenv install` every time you fix a bug in your library
    * **In Development:** This creates a symlink. 
    If you change the code in `./my_local_lib`, the changes are live in your environment immediately.
    * **In Docker:** If you use this, 
    you **must** ensure the folder `./my_local_lib` is also `COPY`ed into the final stage of your Docker image 
    at the same relative path, or the symlink will point to nothing.
* **`editable = false`**: for production Docker images where you want the library to be a static artifact
  * If you set `editable = false` (or omit it), 
  Pipenv effectively "installs" the package by copying the files into the virtual environment's `site-packages` 
  at the time of installation.

### 2. Common Notation Variants

| Type                       | Notation Example                                                     |
|:---------------------------|:---------------------------------------------------------------------|
| **Standard (Any version)** | `requests = "*"`                                                     |
| **Specific Version**       | `flask = "==3.0.0"`                                                  |
| **Version Range**          | `numpy = ">=1.25,<2.0"`                                              |
| **Git Repository**         | `ext-lib = {git = "https://github.com/user/repo.git", ref = "main"}` |
| **Local File (Wheel)**     | `custom-tool = {path = "./dist/tool-0.1-py3-none-any.whl"}`          |
| **Extras**                 | `pandas = {version = "*", extras = ["performance"]}`                 |

