"""
================================================================
Type Conversion
================================================================

3 Types of data in python
1. strings
2. numbers
3. booleans

Following functions can be used for conversions between different types
* int()
* float()
* bool()
* str()
"""

birth_year =  input("Enter your birth year : ")

# age = 2023 - birth_year
# ==> TypeError: unsupported operand type(s) for -: 'int' and 'str'

age = 2023 - int(birth_year)

print(age)

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
sum = num1 + num2
# print("Sum : " + sum) ==> TypeError
print("Sum : ", sum)
