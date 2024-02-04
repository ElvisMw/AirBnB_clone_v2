#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.city import City
from models.state import State

# Table for Many-to-Many relationship between Place and Amenity
metadata = BaseModel.metadata
place_amenit#!/usr/bin/python3
"""
Place Module for HBNB project.

This module defines the Place class, which inherits from BaseModel.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.city import City
from models.state import State

# Table for Many-to-Many relationship between Place and Amenity
metadata = BaseModel.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel):
    """
    A place to stay.

    Attributes:
    - city_id (str): ID of the city where the place is located.
    - user_id (str): ID of the user who owns the place.
    - name (str): Name of the place.
    - description (str): Description of the place.
    - number_rooms (int): Number of rooms in the place.
    - number_bathrooms (int): Number of bathrooms in the place.
    - max_guest (int): Maximum number of guests the place can accommodate.
    - price_by_night (int): Price per night for the place.
    - latitude (float): Latitude coordinate of the place.
    - longitude (float): Longitude coordinate of the place.

    Relationships:
    - amenities (relationship): Many-to-Many relationship with Amenity through place_amenity table.
    - reviews (relationship): One-to-Many relationship with Review.
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship('Amenity', secondary=place_amenity,
                             back_populates='place_amenities', viewonly=False)

    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
y = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship('Amenity', secondary=place_amenity,
                             back_populates='place_amenities', viewonly=False)

    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
