# Pipenv Commands

currently active virtual environment path:
    
    pipenv --venv

install dependencies from Pipfile:

    pipenv install

- `--deploy`: ensures Pipfile.lock is up to date
- `--ignore-pipfile`: uses only the lock file for stability

      pipenv install --deploy --ignore-pipfile

install a specific package and add it to Pipfile:

    pipenv install <PACKAGE_NAME>

install a specific package as a development dependency:

    pipenv install <PACKAGE_NAME> --dev

uninstall a package and remove it from Pipfile:

    pipenv uninstall <PACKAGE_NAME>

run a command inside the virtual environment:

    pipenv run <COMMAND>

spawn a shell within the virtual environment:

    pipenv shell


