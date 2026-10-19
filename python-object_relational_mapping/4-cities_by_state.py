#!/usr/bin/python3
"""List each city and its state from a MySQL database."""

import sys

import MySQLdb


def main():
    """Print cities in ascending city ID order."""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities INNER JOIN states "
             "ON cities.state_id = states.id ORDER BY cities.id ASC")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
