#!/usr/bin/python3
"""Check which list values are divisible by two."""


def divisible_by_2(my_list=[]):
    """Return a boolean for each input integer's divisibility by two."""
    return [number % 2 == 0 for number in my_list]
