#!/usr/bin/python3
"""
This is the "0-read_file" module.
This module supplies one function, read_file().

"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and
    prints it to stdout
    """
    with open(filename, encoding="utf-8") as filed_open:
        print(filed_open.read(), end="")
