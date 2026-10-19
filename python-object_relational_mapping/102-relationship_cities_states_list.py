#!/usr/bin/python3
"""List cities with their states using one eager-loading query."""

import sys
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from relationship_city import City
from relationship_state import Base, State


def main():
    """Print every city and its related state in city ID order."""
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).options(
        joinedload(City.state)).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
    engine.dispose()


if __name__ == "__main__":
    main()
