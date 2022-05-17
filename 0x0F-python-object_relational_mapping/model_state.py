#!/usr/bin/python3
"""
Python file that contains the class definition of a State
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    Class that defines the table states
    """
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
