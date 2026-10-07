#!/usr/bin/python3
"""Create a dictionary with all values doubled."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with each integer value doubled."""
    return {key: value * 2 for key, value in a_dictionary.items()}
