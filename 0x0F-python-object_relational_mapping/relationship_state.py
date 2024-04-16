#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a state with SQLalchemy.

    Attributes:
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
        cities (sqlalchemy.orm.relationship): The state's cities.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete"
    )
