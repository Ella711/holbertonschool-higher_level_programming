#!/usr/bin/python3:
def roman_to_int(roman_string):
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    if roman_string == "":
        return 0
    value = 0
    for x, y in zip(roman_string, roman_string[1:]):
        if x not in roman.keys():
            return 0
        elif roman[x] >= roman[y]:
            value += roman[x]
        else:
            value -= roman[x]
    value += roman[roman_string[-1]]
    return value
