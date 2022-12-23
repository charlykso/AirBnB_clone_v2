#!/usr/bin/python3
"""Defines the DBStorage class"""

from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity

all_classes = {"City": City,
               "State": State,
               "Place": Place,
               "User": User,
               "Review": Review,
               "Amenity": Amenity}



class DBStorage:
    """ Represents the DB engine 

        Attributes:
                __engine (): engine of the db
                __session (): session of the db

    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialises the DBStorage instance """
        self.__engine = create_engine('mysql+msqldb://{}:{}@{}/{}'
                                      .format(
                                          getenv('HBNB_MYSQL_USER'),
                                          getenv('HBNB_MYSQL_PWD'),
                                          getenv('HBNB_MYSQL_HOST'),
                                          getenv('HBNB_MYSQL_DB')
                                          ), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls).
        if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review).
        this method must return a dictionary: (like FileStorage)
        """

        return_dict = {}
        query = []

        if cls:
            for name, value in all_classes.values():
                if name == cls:
                    query = self.__session.query(value)
                    for obj in query:
                        key = name + '.' + obj.id
                        return_dict[key] = obj
            return return_dict
        else:
            for name, value in all_classes.values():
                query = self.__session.query(value)
                for obj in query:
                    key = name + '.' + obj.id
                    return_dict[key] = obj
        return return_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database
        session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        - create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be
        imported before calling Base.metadata.create_all(engine)
        - create the current database session (self.__session)
        from the engine (self.__engine) by using a sessionmaker
        - the option expire_on_commit must be set to False ;
        and scoped_session - to make sure your Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
