#!/usr/bin/python3
"""Define a square with area calculation."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square after validating size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
