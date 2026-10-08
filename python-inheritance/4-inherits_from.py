#!/usr/bin/python3
"""Check whether an object's class inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherits from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
