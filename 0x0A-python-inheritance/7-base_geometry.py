#!/usr/bin/python3
"""
This is the "7-base_geometry" module.
This module supplies one class, BaseGeometry.

"""


class BaseGeometry:
    """
    class that defines the base geometry
    """
    def area(self):
        """function not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
