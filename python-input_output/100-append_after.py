#!/usr/bin/python3
"""Insert text after every line containing a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert ``new_string`` after each matching line in ``filename``."""
    with open(filename, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
