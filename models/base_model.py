#!/usr/bin/python
"""
Module for defining BaseModel class.
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models import storage
import uuid

Base = declarative_base()

class BaseModel:
    """
    Base class for all models.

    Attributes:
    - id (str): Unique identifier for the instance.
    - created_at (DateTime): Timestamp for when the instance was created.
    - updated_at (DateTime): Timestamp for when the instance was last updated.

    Methods:
    - __init__(self, *args, **kwargs): Initializes a BaseModel instance.
    - save(self): Saves the current instance to the storage.
    - delete(self): Deletes the current instance from the storage.
    - to_dict(self): Returns a dictionary representation of the instance.
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.

        Args:
        - args: Variable positional arguments.
        - kwargs: Variable keyword arguments.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k in ('created_at', 'updated_at'):
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k != '__class__':
                    setattr(self, k, v)

    def save(self):
        """
        Save the current instance to the storage.
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def delete(self):
        """
        Delete the current instance from the storage.
        """
        storage.delete(self)

    def to_dict(self):
        """
        Return a dictionary representation of the instance.

        Returns:
        dict: Dictionary representation of the instance.
        """
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        return data
