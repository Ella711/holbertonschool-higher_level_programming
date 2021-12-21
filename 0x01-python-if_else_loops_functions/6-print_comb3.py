#!/usr/bin/python3
for number in range(10):
    for numbers in range(10):
        if number < numbers:
            if number == 8 and numbers == 9:
                print("{}{}".format(number, numbers), end="")
            else:
                print("{}{}, ".format(number, numbers), end="")
