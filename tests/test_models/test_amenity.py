#!/usr/bin/python
"""
Test module for the Amenity model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """
    Test class for Amenity model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """
        Test that the 'name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.name, str)
