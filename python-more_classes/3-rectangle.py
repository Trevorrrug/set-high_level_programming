#!/usr/bin/python3
"""Define rectangles with printable string representations."""


class Rectangle:
    """Represent a rectangle with private dimensions."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle's width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle's perimeter, or zero for an empty side."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with hash characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
