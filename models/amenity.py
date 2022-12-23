#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialises the State class
            Args:
                args: Not used
                kwargs: dictionary format of the class
        """
        super().__init__(*args, **kwargs)
