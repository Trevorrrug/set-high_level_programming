#!/usr/bin/python3
"""Print each integer in a list on its own line."""


def print_list_integer(my_list=[]):
    """Print all integers in ``my_list``."""
    for number in my_list:
        print("{:d}".format(number))
