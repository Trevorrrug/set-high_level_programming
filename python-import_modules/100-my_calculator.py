#!/usr/bin/python3
"""Run a basic calculation selected from command-line arguments."""
import sys


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    left = int(sys.argv[1])
    operator = sys.argv[2]
    right = int(sys.argv[3])
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(
        left, operator, right, operations[operator](left, right)))
