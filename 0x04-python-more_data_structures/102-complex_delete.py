#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()

    for key in new_dict:
        if value == new_dict.get(key, None):
            a_dictionary.pop(key, None)
    return a_dictionary
