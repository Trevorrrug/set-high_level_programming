#!/usr/bin/python3
"""Define a square with a validated size property."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square with its size."""
        self.size = size

    @property
    def size(self):
        """Return the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
