#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:
        commons = set_1.intersection(set_2)
        return commons
    return None
