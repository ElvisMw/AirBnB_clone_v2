#!/usr/bin/python
"""
Module for defining the State class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, relationship

class State(BaseModel, Base):
    """
    State class.

    Attributes:
    - name (str): Name of the state.

    Relationships:
    - cities (relationship): One-to-Many relationship with City, back-referenced as 'state', with cascade behavior 'all, delete-orphan'.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            Return the list of City instances with state_id equals to the current State.id.
            """
            return [city for city in storage.all(City).values() if city.state_id == self.id]
