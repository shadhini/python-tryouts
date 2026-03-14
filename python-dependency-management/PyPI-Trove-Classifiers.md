# PyPI trove classifiers that indicates the project maturity level

In PyPI, project maturity is defined using the **Development Status** trove classifiers. 
These are standardized tags you include in your project's metadata (like `pyproject.toml` or `setup.py`) 
to signal to users how stable and reliable your code is.

## The 7 Levels of Maturity

| Classifier                | Meaning                                                             | Status        |
|---------------------------|---------------------------------------------------------------------|---------------|
| **1 - Planning**          | The project is an idea or in the design phase. No code exists yet.  | Pre-Code      |
| **2 - Pre-Alpha**         | Initial coding has started, but it's not usable for anything yet.   | Experimental  |
| **3 - Alpha**             | The project is functional but likely has bugs and an unstable API.  | Early Testing |
| **4 - Beta**              | Feature-complete but needs more real-world testing and "polishing." | Late Testing  |
| **5 - Production/Stable** | **The Gold Standard.** Safe for general use in real applications.   | Stable        |
| **6 - Mature**            | Highly stable, likely in maintenance mode with very few bugs.       | Rock Solid    |
| **7 - Inactive**          | The project is no longer being maintained or has been abandoned.    | Deprecated    |

---

## How to implement these in your project


**Example `pyproject.toml` snippet:**

```toml
[project]
name = "my-timeseries-lib"
version = "0.1.0"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.13",
]

```



