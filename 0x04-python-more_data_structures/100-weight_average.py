#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        weight = 0
        score = 0
        for pair in my_list:
            a, b = pair
            score += a * b
            weight += b
        return score / weight
    else:
        return 0
