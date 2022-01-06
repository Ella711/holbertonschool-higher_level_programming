#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    score = 0
    for pair in my_list:
        a, b = pair
        score += a * b
        weight += b
    return score / weight
