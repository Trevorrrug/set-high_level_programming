#!/usr/bin/python3
"""Append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append ``text`` to ``filename`` and return its character count."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
