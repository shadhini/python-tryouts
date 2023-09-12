import random


# Generator
def lottery():
    # returns 6 numbers between 16 and 40
    for i in range(6):
        yield random.randint(16, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


if __name__ == '__main__':
    for random_number in lottery():
        print("And the next number is... %d!" % random_number)
