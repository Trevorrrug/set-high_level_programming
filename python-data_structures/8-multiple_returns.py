#!/usr/bin/python3
"""Return a string's length and first character."""


def multiple_returns(sentence):
    """Return the length and first character of ``sentence``."""
    first = sentence[0] if sentence else None
    return (len(sentence), first)
