#!/usr/bin/python3
"""Divide every value in a matrix by a number."""


def matrix_divided(matrix, div):
    """Return a new matrix with its values divided and rounded."""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(value, (int, float))
                    for row in matrix for value in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if matrix and any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in row] for row in matrix]
