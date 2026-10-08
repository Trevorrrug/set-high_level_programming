#!/usr/bin/python3
"""Write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write ``text`` to ``filename`` and return its character count."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
