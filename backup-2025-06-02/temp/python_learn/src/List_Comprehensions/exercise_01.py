# create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

if __name__ == "__main__":
    newlist = [int(number) for number in numbers if number > 0]
    print(newlist)

