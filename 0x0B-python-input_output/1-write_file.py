#!/usr/bin/python3
"""
This is the "1-write_file" module.
This module supplies one function, write_file().

"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as filed_open:
        return filed_open.write(text)
