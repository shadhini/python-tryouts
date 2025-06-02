"""
============================================================================
If Statement
============================================================================

A block of code is denoted by indentations.
In C based programming languages,such as C++, C#, Java, JavaScript,
    a block of code is represented by curly braces.
"""

temperature = 25

if temperature > 30:
    print("It's a hot day !")
    print("Drink a plenty of water.")
elif temperature > 20:  # temperature ==> (20, 30]
    print("It's a nice day !")
elif temperature > 10:  # temperature ==> (10, 20]
    print("It's a bit cold.")
else:
    print("It's cold!")  # temperature <= 10

print("Done")

