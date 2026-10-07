#!/usr/bin/python3
"""Find the key associated with the highest score."""


def best_score(a_dictionary):
    """Return the key with the greatest value, or None if empty."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
