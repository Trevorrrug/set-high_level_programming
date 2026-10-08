#!/usr/bin/python3
"""Find the maximum integer in a list."""


def max_integer(list=[]):
    """Return the largest integer in ``list``, or None if it is empty."""
    if not list:
        return None
    result = list[0]
    index = 1
    while index < len(list):
        if list[index] > result:
            result = list[index]
        index += 1
    return result
