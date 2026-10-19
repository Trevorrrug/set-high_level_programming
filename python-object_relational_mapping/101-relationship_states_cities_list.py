#!/usr/bin/python3
"""List all states and their cities."""

import sys
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from relationship_city import City
from relationship_state import Base, State


def main():
    """Print each state followed by its cities in ID order."""
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (session.query(State)
              .options(joinedload(State.cities))
              .order_by(State.id))
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
    engine.dispose()


if __name__ == "__main__":
    main()
