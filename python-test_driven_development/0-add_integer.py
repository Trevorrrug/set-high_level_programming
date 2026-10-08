#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function that validates and adds two numeric values.
Floating-point values are converted to integers before the addition.
"""


def add_integer(a, b=98):
    """Add two values after converting them to integers.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
