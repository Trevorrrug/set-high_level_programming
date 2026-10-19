#!/usr/bin/python3
"""List states matching a name supplied on the command line."""

import sys

import MySQLdb


def main():
    """Connect to the database and print matching states by ID."""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC".format(sys.argv[4]))
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
