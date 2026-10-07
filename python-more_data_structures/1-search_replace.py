#!/usr/bin/python3
"""Replace matching values in a new list."""


def search_replace(my_list, search, replace):
    """Return a copy of my_list with search replaced by replace."""
    return [replace if value == search else value for value in my_list]
