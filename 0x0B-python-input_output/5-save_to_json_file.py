#!/usr/bin/python3
"""
This is the "5-save_to_json_file" module.
This module supplies one function, save_to_json_file().

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding='utf-8') as filed_opened:
        json.dump(my_obj, filed_opened)
