#!/usr/bin/python3
"""
Python file that contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Class that defines the table states
    """
    __tablename__ = "cities"
    id = Column("id", Integer(), autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer(), ForeignKey("states.id"),
                      nullable=False)
