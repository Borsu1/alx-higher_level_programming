#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa
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
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Creation of the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creation of the new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
