#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity inherits from BaseModel and Base
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

    def __init__(self, *args, **kwargs):
        """ Initialises the State class
            Args:
                args: Not used
                kwargs: dictionary format of the class
        """
        super().__init__(*args, **kwargs)
