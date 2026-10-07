#!/usr/bin/python3
"""Return a new matrix containing the squares of the input values."""


def square_matrix_simple(matrix=[]):
    """Return a squared copy of matrix without modifying it."""
    return [[value * value for value in row] for row in matrix]
