#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        unique_numbers = set(my_list)
        summ = 0
        for number in unique_numbers:
            summ += number
        return summ
    return None
