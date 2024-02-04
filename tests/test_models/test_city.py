#!/usr/bin/python
"""
Test module for the City model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """
    Test class for City model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test that the 'state_id' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.state_id, str)

    def test_name(self):
        """
        Test that the 'name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.name, str)
