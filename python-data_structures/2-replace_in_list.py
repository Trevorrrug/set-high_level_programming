#!/usr/bin/python3
"""Replace an item in a list."""


def replace_in_list(my_list, idx, element):
    """Replace an item at ``idx`` and return the same list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
