## Multi-module Project Vs Project with Sub Projects

| **Multi-Module Project**                                                                                                                                | **Multi-Project Project**                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| different modules or components of the software project are organized within a single codebase or repository                                            | different components or features of the software project are organized as separate codebases or repositories                                    |
| Each module represents a distinct functionality or feature of the project                                                                               | Each project represents a self-contained unit with its own codebase, dependencies, and build process                                            |
| modules are typically interdependent and share the same context, resources, and configuration                                                           | projects are typically independent of each other and can be developed, tested, and deployed separately                                          |
| modules can be compiled and built together, producing a single executable or package                                                                    | Each project may have its own team, release cycle, and deployment strategy                                                                      |
| project can be managed as a single entity, allowing for easier coordination and collaboration between developers                                        | projects can communicate with each other through APIs or other integration mechanisms                                                           |
| Examples of multi-module projects include large-scale web applications with different modules for authentication, user management, and various features | Examples of multi-project projects include microservices architectures, where each microservice is developed and deployed as a separate project |

## Advantages of each type

| **Multi-Module Project**                                                                                                               | **Multi-Project Project**                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Simplicity**: A single codebase makes it easier to navigate, understand, and maintain the project.                                   | **Independence**: Each project can be developed, tested, and deployed independently, providing flexibility.                              |
| **Shared context**: Modules can share resources, configuration, and build processes, promoting consistency.                            | **Scalability**: Projects can be added or removed as needed, enabling scalability and agility.                                           |
| **Collaboration**: Developers can work on different modules within the same project, facilitating collaboration and knowledge sharing. | **Technology diversity**: Different projects can use different technologies or programming languages, catering to specific requirements. |

# Project with Sub Projects Development

### Project Directory Structure

```text
project/
  |- project1/
  |   |- src/
  |   |   |- project1/
  |   |       |- __init__.py
  |   |       |- module1.py
  |   |- tests/
  |   |   |- test_module1.py
  |   |- setup.py
  |   |- Pipfile
  |   |- Pipfile.lock
  |
  |- project2/
  |   |- src/
  |   |   |- project2/
  |   |       |- __init__.py
  |   |       |- module2.py
  |   |- tests/
  |   |   |- test_module2.py
  |   |- setup.py
  |   |- Pipfile
  |   |- Pipfile.lock
  |
  |- README.md
```

### Instructions

> **_Pipenv_** for package management
>
> **_setup.py_** for distribution

1. Create a project directories for each project


2. Initialize Pipenv inside each project directory 
   
   #### by navigating to each subproject's directory
    =>This creates a Pipfile that will manage each project's virtual environment and dependencies
    ```shell
    pipenv --python 3.11
    ```
   #### Through PyCharm

   - Create subprojects (say a and b) in your workspace: 
     - Open each project separately from PyCharm 
       - File --> Open, select directory "a", choose "Attach"
         - this makes the folder look bold in your workspace
       - Settings --> project --> Python Interpreter
         - select project "a" --> configure interpreter --> gear icon,"add", "pipenv interpreter"
       - repeat same for "b"

     ![pycharm-open-multiple-projects.png](resources%2Fpycharm-open-multiple-projects.png)
     ref: https://www.jetbrains.com/help/pycharm/open-projects.html#f112afac
   
   ##### To remove existing virtual environment
   - Settings --> project --> Python Interpreter
   - select the project from which you want to remove the virtual environment
   - expand the `Python Interpreter:` drop down and click on `Show All...` 
   - select the interpreter you want to remove and press the `-` icon in menu bar of that window

3. Add dependencies inside each project's directory
   ```shell
   pipenv install 
   OR
   pipenv install <package>
   ```

4. Remember to activate the appropriate Pipenv environment(virtual environment) for each sub-project when working on them. 

   from the module's directory and run 
   ```shell
   pipenv shell
   ```
