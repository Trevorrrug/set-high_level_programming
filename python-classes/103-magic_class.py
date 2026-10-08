#!/usr/bin/python3
"""Define a circle-like class with area and circumference calculations."""
import math


class MagicClass:
    """Represent a circle with a validated radius."""

    def __init__(self, radius=0):
        """Initialize with an integer or float radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the circle's area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circle's circumference."""
        return 2 * math.pi * self.__radius
