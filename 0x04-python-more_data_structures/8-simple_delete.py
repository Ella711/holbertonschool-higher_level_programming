#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is not None:
        for entries in a_dictionary:
            a_dictionary.pop(key, None)
            return a_dictionary
    else:
        return None
