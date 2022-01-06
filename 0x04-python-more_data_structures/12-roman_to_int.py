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
    for key in roman:
        if key in roman_string.upper():
            idx = roman_string.upper().index(key)
            break
    value = 0
    for letter in roman_string.upper()[idx:]:
        value += roman.get(letter)
    if idx > 0:
        for letter in roman_string.upper()[:idx]:
            value -= roman.get(letter)
    return value
