#!/usr/bin/python3
"""Read and print a UTF-8 text file."""


def read_file(filename=""):
    """Print the contents of ``filename`` to standard output."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
