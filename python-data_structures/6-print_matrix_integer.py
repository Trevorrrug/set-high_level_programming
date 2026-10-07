#!/usr/bin/python3
"""Print a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each matrix row with single spaces between integers."""
    for row in matrix:
        print(" ".join("{:d}".format(number) for number in row))
