#!/usr/bin/python3
"""Print a dictionary in key order."""


def print_sorted_dictionary(a_dictionary):
    """Print first-level key/value pairs sorted alphabetically."""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
