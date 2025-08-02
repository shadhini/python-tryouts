---
icon: '1'
---

# Getting Started

## Using MacOS Command Line

MacOS comes with **Python** **pre-installed**. You can install Python 3 from [python.org](http://python.org/)

```bash
# check version of Python you have installed on your Mac
~ via 💎 v3.1.3
❯ python --version
Python 3.9.13

# check for Python3
~ via 💎 v3.1.3
❯ python3 --version
Python 3.9.13

```



If python 3 is installed in the machine

To write Python code from terminal, @ cmd line type & enter

* `python` → to open python interpreter in terminal
* `exit()` → to close interpreter



```bash
# Python Interpreter
~ via 💎 v3.1.3
❯ python
Python 3.9.13 (main, Aug 25 2022, 18:29:29)
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.


>>> name = "Amritha"
>>> print("Hello " + name + "!")
Hello Amritha!

>>> print(-1/4)
-0.25
>>> print(2**10)
1024
>>> print(((2050/5)-32)/9)
42.0


>>> for i in range(5):
...     print("Hello World!)
  File "<stdin>", line 2
    print("Hello World!)
                        ^
SyntaxError: EOL while scanning string literal
>>> for i in range(5):
...     print("Hello World!")
...
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
>>> exit()

~ via 💎 v3.1.3 took 14s
❯
```



## Using Linux Command Line

```bash
# install python
sudo apt install python3

# run python interpreter on terminal
python3

# exit interpreter
>>> exit()
```



## Using IDLE

Default Python IDE that is included with Python installations on Windows and MacOS. Can be downloaded using package manager on Linux.

IDLE: an interactive interpreter or file editor



```bash
# install IDLE on Linux
sudo apt install idle
```



