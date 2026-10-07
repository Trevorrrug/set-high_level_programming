#!/usr/bin/python3
"""Remove both forms of the letter c from a string."""


def no_c(my_string):
    """Return ``my_string`` without the characters c and C."""
    result = ""
    for character in my_string:
        if character != "c" and character != "C":
            result += character
    return result
