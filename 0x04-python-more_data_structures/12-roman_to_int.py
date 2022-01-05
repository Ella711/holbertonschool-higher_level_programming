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

    if roman_string is not None:
        for key in roman:
            if key in roman_string:
                idx = roman_string.index(key)
                break
        value = 0
        for letter in roman_string[idx:]:
            value += roman.get(letter)
        if idx > 0:
            for letter in roman_string[:idx]:
                value -= roman.get(letter)

        return value



