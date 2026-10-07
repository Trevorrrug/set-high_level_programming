#!/usr/bin/python3
"""Create a copy of a list with one item replaced."""


def new_in_list(my_list, idx, element):
    """Return a copied list with ``idx`` replaced when valid."""
    new_list = my_list[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
