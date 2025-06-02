"""
================================================================
Arithmetic Operations
================================================================

`/`: Division; returns a floating point number; i.e. number with decimal points
`//`: Division; returns an integer; i.e. whole number
`%`: Moduls; returns the remainder of a division
`**`: Exponent

Augmented Assignment Operators
----------------------------------------------------------------
x = x + 3 ==> x += 3
x = x - 3 ==> x -= 3
x = x * 3 ==> x *= 3

Operator Precedence
----------------------------------------------------------------
Same as maths, but we can change it using parentheses

1. Parentheses: `( )`
2. Exponentiation: ``
3. Unary Operators: `+x`, `-x`, `~x`
4. Multiplication, Division, Modulus: `*`, `/`, `//`, `%`
5. Addition and Subtraction: `+`, `-`
6. Bitwise Shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR: `^`
9. Bitwise OR: `|`
10. Comparison Operators: `<`, `<=`, `>`, `>=`, `==`, `!=`
11. Membership Operators: `in`, `not in`
12. Identity Operators: `is`, `is not`
13. Logical NOT: `not`
14. Logical AND: `and`
15. Logical OR: `or`
"""

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Augmented Assignment Operators
x = 10
x **= 3
print(x)

print((10 + 3) * 2)
