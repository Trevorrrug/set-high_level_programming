#!/usr/bin/python3
"""Define a Student class that can restore its attributes from a dict."""


class Student:
    """Represent a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return all or selected instance attributes."""
        if isinstance(attrs, list) and all(
                isinstance(attribute, str) for attribute in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the instance attributes with values from ``json``."""
        for key, value in json.items():
            setattr(self, key, value)
