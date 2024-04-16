#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
Base = declarative_base(). This module uses SQLAlchemy, a SQL toolkit and
Object-Relational Mapping (ORM) system for Python, to interact with a MySQL
database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class represents a state with an id and a name.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Integer): The state's id. It is the primary key.
        name (String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://username:password@localhost:3306/database_name'
    )
    Base.metadata.create_all(engine)
