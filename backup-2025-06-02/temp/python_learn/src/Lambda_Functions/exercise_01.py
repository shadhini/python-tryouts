# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" if not for each element.
l = [2, 4, 7, 3, 14, 19]

if __name__ == '__main__':
    for i in l:
        is_odd = lambda a: (a % 2) == 1
        print(is_odd(i))
