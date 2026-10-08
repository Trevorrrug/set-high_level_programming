#!/usr/bin/python3
"""Return a class instance's dictionary for JSON serialization."""


def class_to_json(obj):
    """Return the attributes of ``obj`` as a dictionary."""
    return obj.__dict__
