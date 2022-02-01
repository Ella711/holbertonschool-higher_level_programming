#!/usr/bin/python3
"""
This is the "6-load_from_json_file" module.
This module supplies one function, load_from_json_file().

"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding='utf-8') as filed_opened:
        return json.load(filed_opened)
