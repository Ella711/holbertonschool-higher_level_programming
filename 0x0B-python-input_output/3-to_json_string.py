#!/usr/bin/python3
"""
This is the "3-to_json_string" module.
This module supplies one function, to_json_string().

"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of an object (string):
    """
    return json.dumps(my_obj)
