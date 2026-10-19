#!/usr/bin/python3
"""Safely list states matching a name supplied on the command line."""

import sys

import MySQLdb


def main():
    """Connect to the database and print matching states by ID."""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
