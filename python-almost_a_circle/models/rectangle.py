#!/usr/bin/python3
"""Define the Rectangle model."""

from models.base import Base


class Rectangle(Base):
    """Represent a rectangle with position and dimensions."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize and validate a rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a positive integer width."""
        self._validate_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a positive integer height."""
        self._validate_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the horizontal position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set a nonnegative integer horizontal position."""
        self._validate_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the vertical position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set a nonnegative integer vertical position."""
        self._validate_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @staticmethod
    def _validate_integer(name, value):
        """Raise TypeError unless value is exactly an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using hash characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the formatted rectangle description."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from positional or keyword arguments."""
        attributes = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the rectangle attributes as a dictionary."""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
