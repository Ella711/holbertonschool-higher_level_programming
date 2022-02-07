#!/usr/bin/python3
"""
This is the "models/rectangle" module.
This module supplies one class, Rectangle.

"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Privatize instance attribute: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set conditions for width attribute and raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Privatize instance attribute: x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set conditions for x attribute and raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Privatize instance attribute: y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set conditions for y attribute and raise exceptions"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle object"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Overrides the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if args is not None and len(args) > 0:
            attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        rect_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return rect_dict
