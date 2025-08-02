# Naming Conventions
- cannot contain spaces
- may be a mixture of upper and lower case characters and numbers; no special characters other than underscore `_`
- can’t start with a number 
- descriptive names are better than cryptic abbreviations
  - `student_name` is better than `sn`
- underscore
  - Single leading underscore (`_variable`): indicates the variable is intended for internal use. 
    - In classes, it suggests the variable is "protected" (should not be accessed directly). 
  - Double leading underscore (`__variable`): Triggers name mangling in classes, making it harder (but not impossible) to access from outside the class. 
  - Single trailing underscore (`variable_`): Used to avoid conflicts with Python keywords (e.g., `class_`).

## Variable & Function names 
- should be written in **`snake_case`**; all letters are lowercase and words are separated using an underscore

