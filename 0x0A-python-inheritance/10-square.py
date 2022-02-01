#!/usr/bin/python3
"""
This is the "10-square" module.
This module supplies one class, Square.

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Child class of Rectangle
    """
    def __init__(self, size):
        """
        Instantiation of private attribute, size,
        validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
