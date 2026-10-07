#!/usr/bin/python3
"""Print a list of integers in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print integers from the end of ``my_list`` to the beginning."""
    if my_list is None:
        return
    for number in my_list[::-1]:
        print("{:d}".format(number))
