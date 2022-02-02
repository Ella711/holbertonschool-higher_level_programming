#!/usr/bin/python3
"""
This is the "7-add_item" module.
Script that adds all arguments to a
Python list, and then save them to a file

"""
from sys import argv


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"

try:
    argv_list = load_from_json_file(filename)
except FileNotFoundError:
    argv_list = []

save_to_json_file(argv_list + argv[1:], filename)
