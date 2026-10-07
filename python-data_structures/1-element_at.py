#!/usr/bin/python3
"""Retrieve an item from a list by index."""


def element_at(my_list, idx):
    """Return the item at ``idx`` or None when the index is invalid."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
