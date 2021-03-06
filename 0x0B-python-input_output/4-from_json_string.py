#!/usr/bin/python3
"""
This is the "4-from_json_string" module.
This module supplies one function, from_json_string().

"""
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string:
    """
    return json.loads(my_str)
