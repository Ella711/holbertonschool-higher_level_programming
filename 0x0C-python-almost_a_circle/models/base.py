#!/usr/bin/python3
"""
This is the "models/base" module.
This module supplies one class, Base.

"""
import json


class Base:
    """
    Base class for all other tasks
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        object_list = []
        if list_objs is not None:
            for objs in list_objs:
                object_list.append(cls.to_dictionary(objs))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as filed_opened:
            filed_opened.write(cls.to_json_string(object_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            json_list = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        inst_list = []
        if filename:
            with open(filename, "r") as filed_opened:
                json_dict = cls.from_json_string(filed_opened.read())
            for i, j_dict in enumerate(json_dict):
                inst_list.append(cls.create(**json_dict[i]))
            return inst_list
        return inst_list


