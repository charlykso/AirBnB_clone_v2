#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class 

        Attributes:
                    __tablename__ : name of the table
                    name (sqlalchemy String): name of the state

    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("cities", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Get a list if all ralated City objects. """
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id = self.id:
                    city_list.append(city)
            return city_list
