#!/usr/bin/python3
"""Print every solution to the N-Queens puzzle."""
import sys


def solve_queens(size):
    """Print all non-attacking queen placements for a board of size."""
    solution = []
    columns = set()
    descending_diagonals = set()
    ascending_diagonals = set()

    def place_queen(row):
        if row == size:
            print(solution)
            return
        for column in range(size):
            descending = row - column
            ascending = row + column
            if (column in columns or descending in descending_diagonals or
                    ascending in ascending_diagonals):
                continue
            solution.append([row, column])
            columns.add(column)
            descending_diagonals.add(descending)
            ascending_diagonals.add(ascending)
            place_queen(row + 1)
            solution.pop()
            columns.remove(column)
            descending_diagonals.remove(descending)
            ascending_diagonals.remove(ascending)

    place_queen(0)


def main():
    """Validate command-line input and print its N-Queens solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_queens(size)


if __name__ == "__main__":
    main()
