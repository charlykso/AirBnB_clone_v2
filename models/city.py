#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City inherits from BaseModel and Base
    __tablename__: represents the table name, cities
    name :  represents a column containing a string (128 characters)
            can’t be null
    state_id :  represents a column containing a string (60 characters)
                can’t be null
                is a foreign key to states.id
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", back_populates="cities", cascade="all")

    def __init__(self, *args, **kwargs):
        """ Initialises the State class
            Args:
                args: Not used
                kwargs: dictionary format of the class
        """
        super().__init__(*args, **kwargs)
