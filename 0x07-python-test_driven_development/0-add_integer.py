#!/usr/bin/python3
"""
This is the "0-add_integer" module.
This module supplies one function, add_integer().

"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
