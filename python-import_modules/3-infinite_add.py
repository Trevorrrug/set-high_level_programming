#!/usr/bin/python3
"""Add all command-line integer arguments."""
import sys


if __name__ == "__main__":
    print(sum(int(argument) for argument in sys.argv[1:]))
