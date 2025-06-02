# Modules
Modules in Python are just Python files with a .py extension.
* The name of the module is the same as the file name.
* A Python module can have a set of functions, classes, or variables defined and implemented.

E.g.: Building a ping pong game
<br />
mygame/
* mygame/game.py --> responsible for the game logic
* mygame/draw.py --> responsible for rendering graphics on the screen

<br />

When importing a module, a `.pyc` file is created. 
* This is a `compiled Python` file. 
* Python compiles files into `Python bytecode` so that it won't have to parse the files each time modules are loaded. 
* If a `.pyc` file exists, it gets loaded instead of the .py file. 
  * This process is transparent to the user.

## Importing module objects to the current namespace
* A `namespace` is a system where every object is named and can be accessed in Python. 
* We import the function `draw_game` into the `main script's namespace` by using the `from` command.

```python
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
```

Here, the name of the module does not precede `draw_game` as `draw.draw_game`, because we've specified the module name using the import command.

### Advantages
* don't have to reference the module over and over

### Disadvantages
* a namespace cannot have 2 objects with the same name, 
  * so the `import` command may replace an existing object in the namespace.

## Importing all objects from a module

```python
from draw import *

def main():
    result = play_game()
    draw_game(result)
```

* This might be a bit risky as changes in the module may affect the module which imports it, 
* but it is shorter and also does not require you to specify which objects you wish to import from the module.

## Custom import name

```python
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
```

## Module initialization

* The `first time a module is loaded into a running Python script`, 
  * it is **initialized by executing the code in the module once**. 
* If `another module in your code imports the same module again`, 
  * it will not be loaded again, so local `variables inside the module act as a "singleton"` 
  * meaning they are initialized only once

```python
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()
```

## Extending module load path
ways to tell the Python interpreter where to look for modules, aside from 
* the default local directory and 
* built-in modules

1. Use the environment variable `PYTHONPATH` to specify additional directories to look for modules
```python
PYTHONPATH=/foo python game.py
```
  * This will execute `game.py`, and will enable the script to load modules from the `foo` directory as well as the local directory.

2. Using the `sys.path.append` function and execute it before running the `import` command
```python
sys.path.append("/foo")
```
  * Now the `foo` directory has been added to the list of paths where modules are looked for.

## Exploring built-in modules
* `urllib` --> enables us to create read data from URLs
  * used for various tasks related to working with URLs, such as 
    * making HTTP requests, 
    * parsing URLs, and 
    * encoding or decoding query parameters. 
```shell
python3.11
```
##### To look for functions implemented in each built-in module you can use `dir` function
e.g: urllib module
```text
>>> import urllib
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'error', 'parse', 'request', 'response']
```

##### To get more information about a particular function, you can use the `help` function
```text
>>> help(urllib.request)
```
OUTPUT
```text
Help on module urllib.request in urllib:

NAME
    urllib.request - An extensible library for opening URLs using a variety of protocols

DESCRIPTION
    The simplest way to use this module is to call the urlopen function,
    which accepts a string containing a URL or a Request object (described
    below).  It opens the URL and returns the results as file-like
    object; the returned object has some extra methods described below.
    
    The OpenerDirector manages a collection of Handler objects that do
    all the actual work.  Each Handler implements a particular protocol or
:
```

### Use built-in modules
```python
import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)
html = response.read()
print(html)
```

# Packages
Packages are `namespaces` containing multiple packages and modules.


## Writing packages

* Each `package` in Python is a `directory` which **MUST** contain a special file called `__init__.py`. 
  * This file, which can be empty, indicates that the directory it's in is a Python package. 
  * That way it can be **imported the same way as a module**.

##### Directory structure
```text
foo/
    __init__.py
    bar/
        __init__.py
example.py
```
##### we can use bar package from example.py as
```python
import foo.bar

foo.bar.bar_func()
```
OR
```python
from foo import bar

bar.bar_func()
```

#####  `__init__.py` file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the `__all__` variable
```python
# __init__.py

__all__ = ["bar"]
```