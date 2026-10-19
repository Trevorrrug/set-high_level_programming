#!/usr/bin/python3
"""Create California and San Francisco through the ORM relationship."""

import sys
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State


def main():
    """Create both tables and insert the related objects."""
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    state.cities.append(City(name="San Francisco"))
    session.add(state)
    session.commit()
    session.close()
    engine.dispose()


if __name__ == "__main__":
    main()
