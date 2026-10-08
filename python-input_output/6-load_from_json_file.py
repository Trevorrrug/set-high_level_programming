#!/usr/bin/python3
"""Load a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the object represented by the JSON in ``filename``."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
