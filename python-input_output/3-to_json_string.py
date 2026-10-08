#!/usr/bin/python3
"""Convert a Python object to its JSON string representation."""
import json


def to_json_string(my_obj):
    """Return ``my_obj`` serialized as JSON."""
    return json.dumps(my_obj)
