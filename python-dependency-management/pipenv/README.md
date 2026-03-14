# Setting up **Pipenv** and Managing Python Dependencies

## 1. Installation and Setup

install Pipenv globally on your system 

```bash
pip install pipenv

```

To initialize a project, navigate to your project folder and specify which version of Python you'd like to use:

```bash
pipenv --python 3.14

```
- This command creates two files: 
  - a `Pipfile` (your list of needs) and 
  - a `Pipfile.lock` (the exact map of every sub-dependency)

- `Pipfile` has Two Buckets of Dependencies
  - `[packages]`: Production dependencies. Your app literally cannot run without these.
  - `[dev-packages]`: These are Development tools. You need them to write, test, and format code, but they aren't part of the final product.

---

## 2. Managing Packages

One of Pipenv's best features is how it categorizes dependencies. 
- You can separate tools you need for coding (like linters) from tools your app needs to run (like Django).

* **Install a production package:**
`pipenv install requests`
  - This will add `requests` to the `[packages]` section of your `Pipfile`.
* **Install a development-only package:**
`pipenv install pytest --dev`
  - This will add `pytest` to the `[dev-packages]` section of your `Pipfile`.
  - When you run `pipenv install` without `--dev`, it will only install the production dependencies, keeping your environment clean for deployment.
  - When to use:
    - testing a new package without affecting the main dependencies
    - experimenting with a tool that might not be needed long-term
    - setting up a local environment
* **Uninstall a package:**
`pipenv uninstall requests`

---

## 3. Running Your Code

### Option A: The "One-Off" Command

If you just want to run a script without "entering" the environment:

```bash
pipenv run python main.py

```

### Option B: Spawning a Shell

If you want to work inside the environment (similar to `source bin/activate` in virtualenv):

```bash
pipenv shell

```

*To leave this mode, simply type `exit`.*

---

## 4. Key Management Commands

As your project grows, you'll use these commands to keep things in sync:

| Command                           | Purpose                                                                         |
|-----------------------------------|---------------------------------------------------------------------------------|
| `pipenv graph`                    | Shows a visual tree of your dependencies (very useful for debugging conflicts). |
| `pipenv check`                    | Scans your dependencies for known security vulnerabilities.                     |
| `pipenv lock`                     | Re-generates the `Pipfile.lock` to ensure your environment is reproducible.     |
| `pipenv install --ignore-pipfile` | Installs exactly what is in the lock file (ideal for production/deployment).    |

---

### Common Troubleshooting

If you ever feel like the environment has become "messy," you can wipe it clean and start fresh based on your Pipfile with one command:
`pipenv --rm && pipenv install`

