#!/usr/bin/python3
"""Provide common ID management and serialization for geometric models."""

import csv
import json


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
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write instances to a JSON file named after their class."""
        dictionaries = []
        if list_objs is not None:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the Python list represented by a JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance and apply its attributes from a dictionary."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Load instances from the class-named JSON file."""
        try:
            with open("{}.json".format(cls.__name__), "r",
                      encoding="utf-8") as file:
                dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write instances to the class-named CSV file."""
        with open("{}.csv".format(cls.__name__), "w", newline="",
                  encoding="utf-8") as file:
            writer = csv.writer(file)
            for obj in list_objs or []:
                if cls.__name__ == "Rectangle":
                    writer.writerow((obj.id, obj.width, obj.height,
                                     obj.x, obj.y))
                else:
                    writer.writerow((obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from the class-named CSV file."""
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="",
                      encoding="utf-8") as file:
                rows = list(csv.reader(file))
        except FileNotFoundError:
            return []
        instances = []
        for row in rows:
            values = [int(value) for value in row]
            if cls.__name__ == "Rectangle":
                data = dict(id=values[0], width=values[1],
                            height=values[2], x=values[3], y=values[4])
            else:
                data = dict(id=values[0], size=values[1],
                            x=values[2], y=values[3])
            instances.append(cls.create(**data))
        return instances

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
