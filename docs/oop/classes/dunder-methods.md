---
icon: underline
---

# Dunder Methods

## Dunder Methods

* `__str__()`: defines string representation of the object
  * When print() method is called on something, Python calls that object’s `__str__()` method and outputs whatever that method returns
  * if `__str__()` is not defined in the class, Python will use the default implementation which returns a string containing the class name and memory address
* `__len__()`: returns the length of the object or collection
* `__contains__()`: tests whether the object contains an item
* `__eq__()`: tests whether two objects are equal



#### default `__str__()` method

```python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
print(honeycrisp) # Output: <__main__.Apple object at 0x107a27d00>
```

#### overriden `__str__()` method @Apple class

```python
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self): # override dunder method
        return f"{self.color} apple with {self.flavor} flavor"

honeycrisp = Apple("red", "sweet")
print(honeycrisp) # Output: red apple with sweet flavor
```



