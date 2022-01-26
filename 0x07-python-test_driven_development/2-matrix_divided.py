#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
This module supplies one function, matrix_divided().

"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_msg)

    quotient_matrix = []
    row_length = len(matrix[0])
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(error_msg)
        if len(lists) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        inner_list = []
        for elements in lists:
            if not isinstance(elements, (int, float)):
                raise TypeError(error_msg)
            inner_list.append(round(elements / div, 2))
        quotient_matrix.append(inner_list)
    return quotient_matrix
