#!/usr/bin/python3
def uppercase(str):
    upper_string = ""
    for i in str:
        char = ord(i)
        if 96 < char < 123:
            upper_string = chr(char - 32)
        else:
            upper_string = i
        print("{}".format(upper_string), end="")
    print("")
