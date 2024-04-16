#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Setup of the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)

    # Creation of the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state
    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()

