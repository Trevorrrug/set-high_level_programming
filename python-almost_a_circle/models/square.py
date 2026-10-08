#!/usr/bin/python3
"""Define the Square model."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle's dimensions and validation."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the square side length."""
        return self.width

    @size.setter
    def size(self, value):
        """Set both dimensions to the validated side length."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the formatted square description."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assign square attributes from positional or keyword arguments."""
        attributes = ("id", "size", "x", "y")
        if args:
            for name, value in zip(attributes, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in attributes:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the square attributes as a dictionary."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
