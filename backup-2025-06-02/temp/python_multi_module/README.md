# Set up a multi-module Python project 
> **_Pipenv_** for package management
>
> **_setup.py_** for distribution
> 
> **_pytest_** for testing

1. Create a project directory

2. Initialize Pipenv inside the project directory

    =>This creates a Pipfile that will manage the project's virtual environment and dependencies
    ```shell
    pipenv --python 3.11
    ```

3. Create the module directories; separate subdirectories for each module and test directories
    ```text
    project/
      |- src/
      |   |- module1/
      |   |   |- __init__.py
      |   |   |- module1.py
      |   |   |- tests/
      |   |       |- test_module1.py     (module specific tests)
      |   |
      |   |- module2/
      |       |- __init__.py
      |       |- module2.py
      |       |- tests/
      |           |- test_module2.py
      |    
      |- setup.py
      |- tests/
      |   |- conftest.py                (project level tests)
      |   |- test_module1.py
      |   |- test_module2.py
      |- Pipfile
      |- Pipfile.lock
    ```
   
4. Remember to activate the appropriate Pipenv environment(virtual environment) for each project when working on them. 

   from the module's directory and run 
   ```shell
   pipenv shell
   ```
   
5. Add project dependencies 
   ```shell
   pipenv install 
   OR
   pipenv install <package>
   ```

6. To distribute the package, create `setup.py` in the project's root directory 
   - `setup.py` 
     - used as a way to distribute the package
     - define the metadata and distribution details 
   ```python
   from setuptools import setup, find_packages
   setup(
        name='python_tryouts',
        version='1.0.0',
        description='Your project description',
        author='Shadhini Jayatilake',
        author_email='shadhini.jayatilake@gmail.com',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=[
            'dependency1',
            'dependency2',
        ],
        tests_require=['pytest'],
   )
   ```

7. Write tests 
   - test files specific to each module
   - project-level tests

8. Run tests
   - This command will discover and execute all the tests in the project
   
   _from the project's root directory_
   ```shell
   pipenv run pytest
   ```

9. Install project and module dependencies 
    - -e flag: ensures that the package is installed in editable mode
   
   _from the project's root directory_
   ```shell
    pipenv install '-e .'
   ```

10. Distribute the project 
    - use the setup.py file to create a distributable package 
    - This generates a dist directory containing the distribution files

   _from the project's root directory_
   ```shell
   python setup.py sdist bdist_wheel
   ```
