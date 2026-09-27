#!/usr/bin/python3
"""Defines the MyInt class."""


class MyInt(int):
    """Represent an integer with inverted equality operators."""

    def __eq__(self, other):
        """Return the inverted result of equality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the inverted result of inequality."""
        return super().__eq__(other)
