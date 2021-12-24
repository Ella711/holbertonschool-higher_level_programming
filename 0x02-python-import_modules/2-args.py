#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = 0
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for arguments in argv:
            args += 1
            if (len(argv) - 1) >= args:
                print("{}: {}".format(args, argv[args]))
