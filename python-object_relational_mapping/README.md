# Python Object-Relational Mapping

This project practices reading and writing MySQL data with `MySQLdb`, mapping
rows to Python objects with SQLAlchemy, and relating State and City models.

## Tasks

- `0`-`5`: select and filter states and cities with MySQLdb.
- `model_state.py`, `6`-`13`: define and query the State model.
- `model_city.py`, `14`: define City and list cities with their state names.
- `relationship_state.py`, `relationship_city.py`, `100`-`102`: create and
  query related State and City objects, including eager-loaded listings.

All command-line scripts keep execution inside a `__main__` guard. The
parameterized queries in tasks 3 and 5 and SQLAlchemy's bound expressions
protect user-supplied values from SQL injection. Task 2 preserves direct string
formatting as required by that exercise; use task 3 for the safe version.
