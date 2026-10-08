#!/usr/bin/python3
"""Print text with paragraph breaks after punctuation."""


def text_indentation(text):
    """Print ``text`` with two newlines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    current_line = ""
    for character in text:
        if character in ".?:":
            current_line += character
            print(current_line.strip(), end="\n\n")
            current_line = ""
        else:
            current_line += character
    if current_line.strip():
        print(current_line.strip(), end="")
