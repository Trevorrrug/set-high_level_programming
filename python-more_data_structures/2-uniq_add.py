#!/usr/bin/python3
"""Sum the unique integers in a list."""


def uniq_add(my_list=[]):
    """Return the sum of each distinct value once."""
    return sum(set(my_list))
