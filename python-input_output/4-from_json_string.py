#!/usr/bin/python3
"""Convert a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by ``my_str``."""
    return json.loads(my_str)
