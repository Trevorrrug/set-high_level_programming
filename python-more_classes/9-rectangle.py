#!/usr/bin/python3
"""Define rectangles with square construction support."""


class Rectangle:
    """Represent a rectangle with comparison and square helpers."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize dimensions and count the new rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return the rectangle drawn with the configured symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        """Return an expression that recreates this rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Announce deletion and update the live instance count."""
        if (hasattr(self, "_Rectangle__width") and
                hasattr(self, "_Rectangle__height")):
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the larger rectangle, preferring rect_1 for equal areas."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a square Rectangle with both dimensions set to size."""
        return cls(size, size)
