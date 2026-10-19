#!/usr/bin/python3
"""Print the cities belonging to a requested state."""

import sys

import MySQLdb


def main():
    """Print matching city names in ascending city ID order."""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT cities.name FROM cities INNER JOIN states "
             "ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4],))
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
