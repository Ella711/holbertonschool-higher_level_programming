#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        squared = []
        squared = [[i * i for i in row] for row in matrix]
        return squared
    return None

# return(list(map(lambda i: i**2, list)) for list in matrix)
