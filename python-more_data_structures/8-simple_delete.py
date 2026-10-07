#!/usr/bin/python3
"""Delete a key from a dictionary when it exists."""


def simple_delete(a_dictionary, key=""):
    """Remove key if present and return the dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
