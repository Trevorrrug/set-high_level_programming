#!/usr/bin/python3
"""Define a list subclass with sorted printing."""


class MyList(list):
    """A list subclass that can print its contents in sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
