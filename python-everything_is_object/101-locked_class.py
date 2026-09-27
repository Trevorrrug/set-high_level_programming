#!/usr/bin/python3
"""Defines the LockedClass."""

class LockedClass:
    """A class that prevents dynamic attributes."""
    __slots__ = ["first_name"]
