#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    State inherits from BaseModel and Base
    __tablename__ : represents the table name, states
    name : represents a column containing a string (128 characters)
    can't be null
    """

    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref='state')
    else:
        @property
        def cities(self):
            """
            FileStorage relationship between State and City.
            getter attribute cities that returns
            the list of City instances with state_id
            equals to the current State.id
            """
            from models import storage
            from models.city import City

            city_list = []
            cities_dict = storage.all(City)

            for city in cities_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
