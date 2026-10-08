#!/usr/bin/python3
"""Provide common ID management and drawing for geometric models."""


class Base:
    """Base class for geometric models."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the model ID, assigning one when omitted."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares in a Turtle graphics window."""
        import turtle

        screen = turtle.Screen()
        screen.title("Rectangles and Squares")
        pen = turtle.Turtle()
        pen.speed(3)

        shapes = [(rectangle, "royalblue")
                  for rectangle in list_rectangles]
        shapes.extend((square, "darkorange") for square in list_squares)

        for shape, color in shapes:
            pen.penup()
            pen.goto(shape.x, shape.y)
            pen.pencolor(color)
            pen.pendown()
            for _ in range(2):
                pen.forward(shape.width)
                pen.left(90)
                pen.forward(shape.height)
                pen.left(90)
            pen.penup()

        pen.hideturtle()
        turtle.done()
