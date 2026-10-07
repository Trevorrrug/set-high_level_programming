#!/usr/bin/python3
"""Delete a list item at a given index."""


def delete_at(my_list=[], idx=0):
    """Delete ``idx`` in place when it is a valid index."""
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
