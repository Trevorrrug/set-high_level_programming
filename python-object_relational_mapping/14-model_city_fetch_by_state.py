#!/usr/bin/python3
"""List cities with their state names using SQLAlchemy."""

import sys
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import Base, State


def main():
    """Print cities in ascending ID order with their state names."""
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id)
    for city, state in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
    engine.dispose()


if __name__ == "__main__":
    main()
