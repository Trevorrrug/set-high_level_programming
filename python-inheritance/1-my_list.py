#!/usr/bin/python3
class MyList(list):
    """A list subclass that can print its contents in sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
