#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Setup of the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name), pool_pre_ping=True
    )

    # Creation of the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the states and cities
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
