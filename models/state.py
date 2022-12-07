#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class State(BaseModel, Base):
    """ State class 

        Attributes:
                    __tablename__ : name of the table
                    name (sqlalchemy String): name of the state

    """
    name = Column(String(128), nullable=False)
