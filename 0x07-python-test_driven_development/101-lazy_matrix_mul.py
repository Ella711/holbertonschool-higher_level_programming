#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
This module supplies one function, lazy_matrix_mul().

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy
    """
    import numpy as np
    return np.matmul(m_a, m_b)
