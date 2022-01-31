#!/usr/bin/python3
"""
This is the "1-my_list" module.
This module supplies one function, my_list().

"""


class MyList(list):
    """
    Class that inherits from list.
    """

    def __init__(self):
        """
        Constructor inherited from list
        """
        super().__init__()

    def print_sorted(self):
        """
        Function that prints a sorted list
        """
        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)
