#!/usr/bin/python
"""
Module for defining the City class.
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    City class.

    Attributes:
    - name (str): Name of the city.

    Relationships:
    - places (relationship): One-to-Many relationship with Place, back-referenced as 'city', with cascade behavior 'all, delete-orphan'.
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='city', cascade='all, delete-orphan')
