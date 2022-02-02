#!/usr/bin/python3
"""
This is the "9-student" module.
This module supplies one class, class Student.
With public method to_json, reload_from_json.
"""


class Student:
    """
    Defines a student by:
    Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor:
        Public instance attributes:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of the class. If attrs not in the keys, skip
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    filtered_dict[attr] = self.__dict__[attr]
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance to the json ones
        """
        for key, value in json.items():
            setattr(self, key, value)
