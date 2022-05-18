#!/usr/bin/python3
"""
Functions to find peak of list of integers
"""


def find_peak(list_of_integers):
    """
    Function to find peak element from list of integers
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    left = 0
    right = length - 1
    while left < right:
        mid = left + (right - left) / 2
        mid = int(mid)
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
