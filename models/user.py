#!/usr/bin/python
"""
Module for defining the User class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    User class.

    Attributes:
    - email (str): Email address of the user.
    - password (str): Password of the user.
    - first_name (str): First name of the user.
    - last_name (str): Last name of the user.

    Relationships:
    - places (relationship): One-to-Many relationship with Place, back-referenced as 'user', with cascade behavior 'all, delete-orphan'.
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade='all, delete-orphan')
