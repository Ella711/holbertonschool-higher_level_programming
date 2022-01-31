#!/usr/bin/python3
"""
This is the "4-inherits_from" module.
This module supplies one function, inherits_from().

"""


def inherits_from(obj, a_class):
    """
    Function returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
