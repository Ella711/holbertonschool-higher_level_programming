#!/usr/bin/python3
"""
This is the "1-my_list" module.
This module supplies one function, my_list().

"""


class MyList(list):
    """
    Class that inherits from list.
    """

    def print_sorted(self):
        """
        Function that prints a sorted list
        """
        print(sorted(self))
