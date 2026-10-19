#!/usr/bin/python3
"""Create the states table using the State SQLAlchemy model."""

import sys
from urllib.parse import quote_plus

from sqlalchemy import create_engine

from model_state import Base, State


def main():
    """Create the states table in the selected database."""
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    engine.dispose()


if __name__ == "__main__":
    main()
