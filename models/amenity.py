#!/usr/bin/python3
"""
Amenity Module for HBNB project.

This module defines the Amenity class, which inherits from BaseModel.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel):
    """
    Amenity class.

    Attributes:
    - name (str): Name of the amenity.

    Relationships:
    - place_amenities (relationship): Many-to-Many relationship with Place through place_amenity table.
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship('Place', secondary=place_amenity,
                                   back_populates='amenities')
