#!/usr/bin/python
"""
Test module for the Place model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """
    Test class for Place model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test that the 'city_id' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.city_id, str)

    def test_user_id(self):
        """
        Test that the 'user_id' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.user_id, str)

    def test_name(self):
        """
        Test that the 'name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.name, str)

    def test_description(self):
        """
        Test that the 'description' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.description, str)

    def test_number_rooms(self):
        """
        Test that the 'number_rooms' attribute is an int.
        """
        new = self.model_instance
        self.assertIsInstance(new.number_rooms, int)

    def test_number_bathrooms(self):
        """
        Test that the 'number_bathrooms' attribute is an int.
        """
        new = self.model_instance
        self.assertIsInstance(new.number_bathrooms, int)

    def test_max_guest(self):
        """
        Test that the 'max_guest' attribute is an int.
        """
        new = self.model_instance
        self.assertIsInstance(new.max_guest, int)

    def test_price_by_night(self):
        """
        Test that the 'price_by_night' attribute is an int.
        """
        new = self.model_instance
        self.assertIsInstance(new.price_by_night, int)

    def test_latitude(self):
        """
        Test that the 'latitude' attribute is a float.
        """
        new = self.model_instance
        self.assertIsInstance(new.latitude, float)

    def test_longitude(self):
        """
        Test that the 'longitude' attribute is a float.
        """
        new = self.model_instance
        self.assertIsInstance(new.longitude, float)

    def test_amenity_ids(self):
        """
        Test that the 'amenity_ids' attribute is a list.
        """
        new = self.model_instance
        self.assertIsInstance(new.amenity_ids, list)
