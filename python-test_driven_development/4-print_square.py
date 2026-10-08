#!/usr/bin/python3
"""Print a square made of hash characters."""


def print_square(size):
    """Print a ``size`` by ``size`` square."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
