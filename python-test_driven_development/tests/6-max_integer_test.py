#!/usr/bin/python3
"""Unit tests for the max_integer function."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer on empty, ordered, and varied lists."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_item(self):
        self.assertEqual(max_integer([7]), 7)

    def test_increasing_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_decreasing_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_maximum_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_negative_values(self):
        self.assertEqual(max_integer([-10, -2, -5]), -2)

    def test_repeated_maximum(self):
        self.assertEqual(max_integer([5, 9, 9, 2]), 9)


if __name__ == "__main__":
    unittest.main()
