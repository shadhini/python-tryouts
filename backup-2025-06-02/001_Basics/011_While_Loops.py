"""
============================================================================
While Loops
============================================================================

"""

i = 1
while i <= 1_000:  # by separating thousands with _, it makes the code more readable
    p = (i//100)
    print('*' * p)  # when string is multiplied by a number, it will repeat the string that many times
    i += 100

