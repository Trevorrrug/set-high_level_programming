#!/usr/bin/python3
"""Reproduce the behavior of the supplied bytecode."""
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """Perform the operation represented by the bytecode."""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
