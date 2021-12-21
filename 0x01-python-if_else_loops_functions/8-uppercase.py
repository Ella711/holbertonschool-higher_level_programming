#!/usr/bin/python3
def uppercase(str):
    upper_string = ""
    for i in range(len(str)):
        char = ord(str[i])
        if 96 < char < 123:
            upper_string += chr(char - 32)
        else:
            upper_string += str[i]
    print(upper_string)
