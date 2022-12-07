#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name 

        Attributes:
                __tablename__ (): name of table for class
                name (sqlalchemy String): name of state
                state_id (sqlalchemy String): state id

    """
    __tablename__ = "cities"
    state_id = Column(String(128), nullable=False)
    name = Column(String(60), nullable=False, foreign_key=states.id)
