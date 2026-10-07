#!/usr/bin/python3
"""Print public names from the hidden_4 module."""

if __name__ == "__main__":
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
