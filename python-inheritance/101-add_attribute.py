#!/usr/bin/python3
"""Defines a function for adding attributes to objects."""


def add_attribute(obj, name, value):
    """Add an attribute to an object when possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
        return
    raise TypeError("can't add new attribute")
