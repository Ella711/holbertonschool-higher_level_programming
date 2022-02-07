#!/usr/bin/python3
"""
This is the "models/square" module.
This module supplies one class, Square.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter for size attribute set to same as Rectangle width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute. Set as width and height of class Rectangle
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - " \
               f"{self.size}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        if args is not None and len(args) > 0:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
