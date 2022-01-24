#!/usr/bin/python3
"""
This is the "0-rectangle" module.
This module supplies one class, Rectangle.

"""


class Rectangle:
    """
    Class that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize attributes with optionals: width, height"""
        self.height = height
        self.width = width
        Rectangle.print_symbol = self.print_symbol

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Privatize instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set conditions for width attribute and raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Privatize instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set conditions for height attribute and raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a Rectangle object"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a Rectangle object"""
        if self.__height == 0 and self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __repr__(self):
        """Represents a class's objects as a string"""
        return "Rectangle(%d, %d)" % (self.__width, self.__height)

    def __str__(self):
        """String representation of a rectangle filled with print_symbol"""
        string_rep = ""
        if self.__height == 0 or self.__width == 0:
            return string_rep

        string_rep += "\n".join([str(self.print_symbol) * self.__width
                                 for rows in range(self.__height)])
        return string_rep

    def __del__(self):
        """Catches when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares area of two instances"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new instance of Rectangle with same height/width"""
        return cls(size, size)
