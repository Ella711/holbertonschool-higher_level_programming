#!/usr/bin/python3
"""
This is the "2-is_same_class" module.
This module supplies one function, is_same_class().

"""


def is_same_class(obj, a_class):
    """
    Function returns true if it's same instance as specified class
    """
    return type(obj) == a_class
