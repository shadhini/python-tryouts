# Write a generator function which returns the Fibonacci series.
# They are calculated using the following formula:
#   The first two numbers of the series is always equal to 1,
#   and each consecutive number returned is the sum of the last two numbers.
# Hint:
#   Can you use only two variables in the generator function?
#   Remember that assignments can be done simultaneously.
import types


def fibonacci():
    a, b = 1, 1
    yield a
    yield b
    while True:
        yield a+b
        a, b = b, a+b


if __name__ == '__main__':
    if type(fibonacci()) == types.GeneratorType:
        print("Good, The fibonacci function is a generator.")
        counter = 0
        for n in fibonacci():
            print(n)
            counter += 1
            if counter == 10:
                break
