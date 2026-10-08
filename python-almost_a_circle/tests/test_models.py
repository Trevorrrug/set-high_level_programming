#!/usr/bin/python3
"""Test Base, Rectangle, and Square models."""

import contextlib
import io
import json
import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base identifiers and serialization helpers."""

    def test_ids_and_json_helpers(self):
        old_count = Base._Base__nb_objects
        try:
            Base._Base__nb_objects = 0
            self.assertEqual(Base().id, 1)
            self.assertEqual(Base(25).id, 25)
            self.assertEqual(Base().id, 2)
        finally:
            Base._Base__nb_objects = old_count
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        data = [{"id": 3, "width": 4}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)
        self.assertEqual(Base.from_json_string(json.dumps(data)), data)

    def test_draw(self):
        calls = []

        class FakePen:
            """Record pen calls made by Base.draw."""

            def __getattr__(self, name):
                def record(*args):
                    calls.append((name, *args))
                return record

        fake_turtle = SimpleNamespace(
            Screen=lambda: SimpleNamespace(
                title=lambda value: calls.append(("title", value))),
            Turtle=lambda: FakePen(),
            done=lambda: calls.append(("done",)))
        rect = SimpleNamespace(x=1, y=2, width=3, height=4)
        square = SimpleNamespace(x=5, y=6, width=7, height=7)
        with patch.dict("sys.modules", {"turtle": fake_turtle}):
            Base.draw([rect], [square])
        self.assertEqual(calls.count(("goto", 1, 2)), 1)
        self.assertEqual(calls.count(("goto", 5, 6)), 1)
        self.assertEqual(calls[-1], ("done",))

    def test_json_file_helpers(self):
        rectangle = Rectangle(4, 5, 6, 7, 100)
        square = Square(8, 9, 10, 103)
        with tempfile.TemporaryDirectory() as folder:
            current = os.getcwd()
            try:
                os.chdir(folder)
                Rectangle.save_to_file([])
                with open("Rectangle.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
                Rectangle.save_to_file([Rectangle(1, 2)])
                self.assertEqual(Rectangle.load_from_file()[0].area(), 2)
                Rectangle.save_to_file([rectangle])
                self.assertEqual(Rectangle.load_from_file()[0].to_dictionary(),
                                 rectangle.to_dictionary())
                Square.save_to_file([square])
                self.assertEqual(Square.load_from_file()[0].to_dictionary(),
                                 square.to_dictionary())
                Square.save_to_file([Square(1)])
                self.assertEqual(Square.load_from_file()[0].size, 1)
                Square.save_to_file([])
                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
                Square.save_to_file(None)
                self.assertEqual(Square.load_from_file(), [])
                os.remove("Square.json")
                self.assertEqual(Square.load_from_file(), [])
            finally:
                os.chdir(current)

    def test_csv_file_helpers(self):
        rectangle = Rectangle(4, 5, 6, 7, 101)
        square = Square(8, 9, 10, 102)
        with tempfile.TemporaryDirectory() as folder:
            current = os.getcwd()
            try:
                os.chdir(folder)
                Rectangle.save_to_file_csv([rectangle])
                Square.save_to_file_csv([square])
                self.assertEqual(
                    Rectangle.load_from_file_csv()[0].to_dictionary(),
                    rectangle.to_dictionary())
                loaded = Square.load_from_file_csv()[0].to_dictionary()
                self.assertEqual(loaded, square.to_dictionary())
                os.remove("Square.csv")
                self.assertEqual(Square.load_from_file_csv(), [])
            finally:
                os.chdir(current)


class TestRectangle(unittest.TestCase):
    """Test Rectangle validation, formatting, and serialization."""

    def test_save_empty_values(self):
        with tempfile.TemporaryDirectory() as folder:
            current = os.getcwd()
            try:
                os.chdir(folder)
                Rectangle.save_to_file(None)
                with open("Rectangle.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
                Rectangle.save_to_file([])
                with open("Rectangle.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
            finally:
                os.chdir(current)

    def test_required_constructor_cases(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual((rectangle.width, rectangle.height), (1, 2))
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual((rectangle.x, rectangle.y), (3, 0))
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual((rectangle.x, rectangle.y), (3, 4))
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.id, 5)

    def test_required_invalid_constructor_cases(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_validation_and_properties(self):
        rectangle = Rectangle(3, 4)
        for name, value in (("width", "3"), ("height", 1.5),
                            ("x", True), ("y", None)):
            message = name + " must be an integer"
            with self.assertRaisesRegex(TypeError, message):
                setattr(rectangle, name, value)
        for name, value, message in (("width", 0, "width must be > 0"),
                                     ("height", -1, "height must be > 0"),
                                     ("x", -1, "x must be >= 0"),
                                     ("y", -1, "y must be >= 0")):
            with self.assertRaisesRegex(ValueError, message):
                setattr(rectangle, name, value)
        rectangle.width = 6
        self.assertEqual(rectangle.width, 6)

    def test_area_display_and_string(self):
        rectangle = Rectangle(2, 2, 1, 1, 7)
        self.assertEqual(rectangle.area(), 4)
        self.assertEqual(str(rectangle), "[Rectangle] (7) 1/1 - 2/2")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rectangle.display()
        self.assertEqual(output.getvalue(), "\n " + "##\n " + "##\n")

    def test_required_display_cases(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            Rectangle(4, 6).display()
        self.assertEqual(output.getvalue(), "####\n" * 6)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            Rectangle(2, 2, 1).display()
        self.assertEqual(output.getvalue(), " ##\n ##\n")

    def test_update_and_dictionary(self):
        rectangle = Rectangle(2, 3)
        rectangle.update(8, 4, 5, 6, 7)
        self.assertEqual(str(rectangle), "[Rectangle] (8) 6/7 - 4/5")
        rectangle.update(x=9, height=10, ignored=1)
        self.assertEqual(rectangle.to_dictionary(),
                         {"id": 8, "width": 4, "height": 10,
                          "x": 9, "y": 7})
        rectangle.update(id=11, width=12)
        self.assertEqual(rectangle.id, 11)


class TestSquare(unittest.TestCase):
    """Test Square inheritance, validation, and serialization."""

    def test_save_empty_values(self):
        with tempfile.TemporaryDirectory() as folder:
            current = os.getcwd()
            try:
                os.chdir(folder)
                Square.save_to_file(None)
                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
                Square.save_to_file([])
                with open("Square.json", encoding="utf-8") as file:
                    self.assertEqual(file.read(), "[]")
            finally:
                os.chdir(current)

    def test_required_constructor_cases(self):
        square = Square(1)
        self.assertEqual(square.size, 1)
        square = Square(1, 2)
        self.assertEqual((square.x, square.y), (2, 0))
        square = Square(1, 2, 3)
        self.assertEqual((square.x, square.y), (2, 3))
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.id, 4)

    def test_required_invalid_constructor_cases(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_string_and_area(self):
        square = Square(5, 2, 3, 9)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.area(), 25)
        self.assertEqual(str(square), "[Square] (9) 2/3 - 5")
        square.size = 8
        self.assertEqual((square.width, square.height), (8, 8))
        with self.assertRaisesRegex(TypeError,
                                    "width must be an integer"):
            square.size = "4"

    def test_update_and_dictionary(self):
        square = Square(2)
        square.update(8, 4, 5, 6)
        self.assertEqual(str(square), "[Square] (8) 5/6 - 4")
        square.update(size=7, y=3)
        self.assertEqual(square.to_dictionary(),
                         {"id": 8, "size": 7, "x": 5, "y": 3})
        square.update(id=12)
        self.assertEqual(square.id, 12)


if __name__ == "__main__":
    unittest.main()
