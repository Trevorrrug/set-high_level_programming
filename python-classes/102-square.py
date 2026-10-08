#!/usr/bin/python3
"""Define a square that supports comparisons by area."""


class Square:
    """Represent a square that can be compared by its area."""

    def __init__(self, size=0):
        """Initialize a square with a non-negative numeric size."""
        self.size = size

    @property
    def size(self):
        """Return the square's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size after validation."""
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __lt__(self, other):
        """Return whether this square has a smaller area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Return whether this square has an area no larger than other."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __eq__(self, other):
        """Return whether both squares have the same area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Return whether both squares have different areas."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __gt__(self, other):
        """Return whether this square has a larger area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Return whether this square has an area no smaller than other."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
