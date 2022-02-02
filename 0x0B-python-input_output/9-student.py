#!/usr/bin/python3
"""
This is the "9-student" module.
This module supplies one class, class Student.
With public method to_json

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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
