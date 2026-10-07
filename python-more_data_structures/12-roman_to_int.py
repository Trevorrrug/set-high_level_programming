#!/usr/bin/python3
"""Convert Roman numerals to integers."""


def roman_to_int(roman_string):
    """Convert a valid Roman numeral from 1 through 3999 to an integer."""
    if not isinstance(roman_string, str):
        return 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    previous = 0
    for symbol in reversed(roman_string):
        value = values.get(symbol, 0)
        if value < previous:
            total -= value
        else:
            total += value
        previous = value
    return total
