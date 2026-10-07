#!/usr/bin/python3
"""Find the largest integer in a list."""


def max_integer(my_list=[]):
    """Return the greatest integer, or None for an empty list."""
    if not my_list:
        return None
    largest = my_list[0]
    for number in my_list[1:]:
        if number > largest:
            largest = number
    return largest
