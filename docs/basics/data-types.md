---
description: Dynamic Typing | Duck Typing | Type Annotations | Type Conversion
icon: square-root-variable
---

# Data Types

## Dynamic Typing

> **— type of variable can change over time as new values are assigned to it —**&#x20;

* Many languages, such as C# or Java, require you to declare variable types, but not Python.



## Duck Typing

> **— Python will infer the variable type at runtime and decide which behaviors are available to the given object —**&#x20;
>
> Python does not enforce type checking at compile time, but rather at runtime.

comes from the saying, <kbd>“If it walks like a duck and quacks like a duck, it must be a duck.”</kbd>

```python
a = "Hello world"      #looks like a string
```



## Type Annotations

{% hint style="success" %}
Type annotations are **optional** in Python.
{% endhint %}

There are 2 ways to annotate a variable with type.

1. Annotating variables directly
   * useful in object-oriented programming when working with custom types
2. Annotating variables with type comments
   * useful for cases when you need to know what types belong to which variables but do not want the overhead of using a line interpreter (linter) or IDE on this specific variable as the interpreter will ignore the comments



### How type annotations affect runtime behavior

{% hint style="danger" %}
Any time a **library is called**, or an IDE works to **scan your code**,&#x20;

╰┈➤ **more computational overhead** is required.
{% endhint %}

{% hint style="success" %}
**Be strategic when annotating variables by type.**&#x20;

╰┈➤ This can add unnecessary overhead when overused.

* In data science, it can be burdensome to manually map data every time a new set of data comes in.
* When doing object-oriented programming or writing functions, using type annotations becomes extremely important because it helps clarify code since you are dealing with more than just the built-in types
{% endhint %}



## Type Conversion

### Implicit Conversion

> **— when the Python interpreter automatically converts one data type to another —**&#x20;

* some data types can be mixed and matched due to implicit conversion

### Explicit Conversion

> **— when code is written to manually convert one data type to another using a data type conversion function —**&#x20;

* type conversion functions
  * `str()` - converts a value (often numeric) to a **string** data type
  * `int()` - converts a value (usually a float) to an **integer** data type
  * `float()` - converts a value (usually an integer) to a **float** data type



***

[GitHub - Jupyter Notebook on Data Types](https://github.com/shadhini/python-tryouts/blob/main/basics/data-types.ipynb)



