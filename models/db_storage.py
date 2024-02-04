#!/usr/bin/python3
"""
Module for defining the DBStorage class.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base


class DBStorage:
    """
    DBStorage class.

    Attributes:
    - __engine (Engine): SQLAlchemy engine.
    - __session (ScopedSession): Scoped SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance.

        Sets up the SQLAlchemy engine and performs additional actions for testing environment.
        """
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', default='localhost')
        database = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query the current database session for objects.

        Args:
        - cls (class): Class filter for querying.

        Returns:
        dict: Dictionary containing objects queried from the session.
        """
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = f'{type(obj).__name__}.{obj.id}'
                objects[key] = obj
        else:
            for clazz in Base.__subclasses__():
                for obj in self.__session.query(clazz).all():
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        return objects

    def new(self, obj):
        """
        Add the object to the current database session.

        Args:
        - obj (BaseModel): Object to be added to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.

        Args:
        - obj (BaseModel): Object to be deleted from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create the current database session.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
