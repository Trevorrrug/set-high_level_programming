#!/usr/bin/python3
"""Define a Student class with JSON-compatible attributes."""


class Student:
    """Represent a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the instance attributes as a dictionary."""
        return self.__dict__
