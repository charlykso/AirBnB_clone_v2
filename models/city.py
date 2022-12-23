#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import ForeignKey, Column, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name 

        Attributes:
                __tablename__ (): name of table for class
                name (sqlalchemy String): name of state
                state_id (sqlalchemy String): state id

    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialises the State class
            Args:
                args: Not used
                kwargs: dictionary format of the class
        """
        super().__init__(*args, **kwargs)
