# Python Interpreter
***
* Operates similar to Unix Shell
  * When called with standard input connected to a tty(terminal control functions) device, 
  
    ⇒ it reads and executes commands interactively;
  
  * when called with a file name argument or with a file as standard input, 
  
    ⇒ it reads and executes a script from that file.

## Installed @
* usually installed as `/usr/local/bin/python3.11`
  * to invoke interpreter through a shell command, put `/usr/local/bin` in your **Unix shell’s search path**
    ```shell
    python3.11
    ```
* `/usr/local/python` is a popular alternative location


* The choice of the directory where the interpreter lives is an installation option
  * to find where it is installed on MacOS
  ```shell
  whereis python3.11
  ```

## Start Interpreter

#### by typing the command below to the shell
```shell
python3.11
```

#### Using python -c command [arg]
```shell
python -c "print('Hello, World!')"
```
* Since Python statements often contain spaces or other characters that are special to the shell,

  ⇒ it is usually advised to quote the command in its entirety.

## Exit interpreter
exit with a zero exit status
* `Control-D` on Unix
* `Control-Z` on Windows
* or by typing the following command: 
  ```shell
  quit()
  ```

## Interpreter’s line-editing features 
* interactive editing
* history substitution 
* code completion on systems that support the GNU Readline library. 

### Check whether command line editing is supported 
Type `Control-P` to the first Python prompt you get. 
* If it beeps, ⇒ you have command line editing
* If nothing appears to happen, or if `^P` is echoed, ⇒ command line editing isn’t available
  * you’ll only be able to use backspace to remove characters from the current line



## Invoking modules as scripts
executes the source file for module as if you had spelled out its full name on the command line.

> python -m module [arg]  


### Non-interactive mode

```shell
python3.11 -m <MODULE_NAME> <ARGUMENT_VALUE>
```
e.g: invoke from the <PROJECT_ROOT_DIR>/python_interpreter directory
```shell
cd src/module_as_scripts/
python3.11 -m interactive_module "test argument"
```
OUTPUT
```text
Running src/module_as_scripts/interactive_module.py as a script
The 1st argument is: test argument
Other arguments are: []
```

### Interactive mode

The interpreter is in `interactive mode`, When commands are read from a **tty**.  
```shell
python3.11 -i -m <MODULE_NAME> <ARGUMENT_VALUE>
```

```text
>>> interactive_module_function(<ARGUMENT_VALUE>)
```

In this mode 
* it prompts for the next command with the primary prompt `>>>`
* for continuation lines it prompts with the secondary prompt `...`
  * Continuation lines are needed when entering a multi-line construct
  ```text
  >>>>> the_world_is_flat = True
  >>>>> if the_world_is_flat:
  ...	    print("Be careful not to fall off!")
  ...
  Be careful not to fall off!
  ```

e.g.:
```shell
cd src/module_as_scripts/
python3.11 -i -m interactive_module "test argument 1" "test argument 2" "test argument 3"
```
OUTPUT
```text
Running src/module_as_scripts/interactive_module.py as a script
The 1st argument is: test argument 1
Other arguments are: ['test argument 2', 'test argument 3']
>>> 
```
---

@interactive mode prompt
```text
>>> interactive_module_function("test argument X for arg0", "test argument Y for arg1", "test argument Z for args")
```

OUTPUT
```text
Running test argument X for arg0 as a script
The 1st argument is: test argument Y for arg1
Other arguments are: test argument Z for args
```

# Argument Passing 
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module. 
* The **length** of the list is at least one
* When `no script` and no arguments are given 

  → sys.argv[0] is an empty string
* When the script name is given as `'-'` (meaning standard input),  

  → sys.argv[0] is set to '-'
* When `-c` command is used, 

  → sys.argv[0] is set to '-c'
* When `-m` module is used, 
  
  → sys.argv[0] is set to the full name of the located module
* Options found after -c command or -m module are not consumed by the Python interpreter’s option processing 

  → but left in sys.argv for the command or module to handle

```python
import sys

def interactive_module_function(arg):
    print(f"The argument is: {arg}")

if __name__ == '__main__':
    args = sys.argv
    interactive_module_function(args[1])
```

# Source Code Encoding
By default, Python source files are treated as encoded in `UTF-8`. 

* To declare an encoding other than the default one, a special comment line should be added as the first line of the file.
  * When encoding is one of the valid codecs supported by Python
    ```text
    # -*- coding: encoding -*-
    ```
  * to declare that Windows-1252 encoding is to be used
    ```text
    # -*- coding: cp1252 -*-
    ```
* when the source code starts with a UNIX `“shebang”` line the encoding declaration should be added as the second line of the file.
  ```text
  #!/usr/bin/env python3
  # -*- coding: cp1252 -*-
  ```
