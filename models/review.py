#!/usr/bin/python
"""
Module for defining the Review class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """
    Review class.

    Attributes:
    - text (str): Text content of the review.
    - place_id (str): ID of the place associated with the review.
    - user_id (str): ID of the user who wrote the review.
    """

    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
