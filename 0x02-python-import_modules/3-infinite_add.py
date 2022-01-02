#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    addition = 0
    if len(argv) > 1:
        for args in range(1, len(argv)):
            addition += int(argv[args])
    print(addition)