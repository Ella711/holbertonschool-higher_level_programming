#!/usr/bin/python3
"""
This is the "12-pascal_triangle" module.
This module supplies one function, pascal_triangle().

"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        inner_list = [1]
        for i in range(rows):
            inner_list.append(triangle[-1][i] + triangle[-1][i+1])
        inner_list.append(1)
        triangle.append(inner_list)
    return triangle
