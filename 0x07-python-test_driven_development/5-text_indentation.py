#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
This module supplies one function, text_indentation().

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    split_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised_text = "\n".join(split_lines)
    print(revised_text, end="")



