---
icon: circle-c
---

# Classes

## Classes in Python

— A class bundles data and functionality together.—&#x20;

Creating a class instance calls a special method called the **constructor**, which initializes the object.

### Constructor method

* method signature: `__init__(self, ...)`
* first parameter of constructor method always should be `self`
* `self` refers to the instance of the class that is being created
* constructor can take any number of arguments

```python
class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"
```

```python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor) # Output: sweet
print(fuji.flavor) # Output: tart
```





## Other special methods: Dunder methods

**`dunder`** <-- double underscore

Python classes have many special methods.

* most of these have default implementations provided by the Python standard library
* but you are free to override the behavior of any of them



Dunder Methods

{% content-ref url="dunder-methods.md" %}
[dunder-methods.md](dunder-methods.md)
{% endcontent-ref %}



## Operator Overriding

> **Special operators:**
>
> built-in symbols or keywords that provide specific behavior with certain data types or objects

{% hint style="info" %}
**Common Special Operators**

* Arithmetic operators: **`+` , `-` , `*` , `/` , `**`**&#x20;
* Comparison operators: **`==` , `!=` , `<` ,  `>=`**&#x20;
* Logical operators: **`and`, `or`, `not`**
* Assignment operators:  **`=` , `+=` , `%=`**&#x20;
{% endhint %}



### Overriding Operators with Dunder Methods

* Each special operator has a corresponding dunder (double underscore) method that implements the operation.
* You can change how an operator behaves by overriding its implementation in your class.



#### E.g: override the `+` operator to add the areas of two triangles

```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()

triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
```

```
Output:
The area of triangle 1 is 25.0
The area of triangle 2 is 24.0
The area of both triangles is 49.0
```





