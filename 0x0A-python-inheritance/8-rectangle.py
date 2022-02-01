#!/usr/bin/python3
"""
This is the "8-rectangle" module.
This module supplies one class, Rectangle.

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class child of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation of private attributes,
        width and height, validated by integer_validator
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
