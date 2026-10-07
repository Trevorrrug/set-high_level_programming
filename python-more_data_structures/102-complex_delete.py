#!/usr/bin/python3
"""Delete every dictionary key whose value matches a target."""


def complex_delete(a_dictionary, value):
    """Remove all matching entries and return the modified dictionary."""
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
