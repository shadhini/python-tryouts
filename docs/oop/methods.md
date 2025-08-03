---
description: Methods in Python
icon: function
---

# Methods

## Methods

### Methods in Python

Behaviors associated with object attributes that modify the state of that object.

They are functions belonging to a specific instance of a class; Functions that operate on the attributes of a specific instance of a class.

***

### Types of Methods

1. **Instance Methods**:
   * most common type
   * defined within a class
     * can access instance-specific data using `self`&#x20;
     * `self` refers to the instance of the class&#x20;
       * e.g: `self.name` retrieves the `name` attribute of the instance
2. **Class Methods**:
   * operate on the class itself, useful for shared data across all instances of the class
   * defined with the `@classmethod` decorator
   * take `cls` as the first parameter, which refers to the class itself
   * can access class-specific data using `cls`
   * used for factory methods or methods that need to modify class-level data
3. **Static Methods**:
   * do not access instance or class-specific data
   * defined with the `@staticmethod` decorator
   * behave like plain functions
   * do not take `self` or `cls` as parameters
   *   can call them directly on the class without creating an instance

       * the methods just reside in the class; this is because class definitions are themselves an object (i.e., an instance of abstract base class), which reduces overhead and allows functions to be encapsulated in an easy-to-use encapsulation.



### Choosing Method Types:

* Use instance methods for individual object data.
* Use class methods for shared data.
* Use static methods for related tasks that don't require access to object or class data.

