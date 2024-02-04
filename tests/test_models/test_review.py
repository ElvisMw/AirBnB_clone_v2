#!/usr/bin/python
"""
Test module for the Review model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """
    Test class for Review model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test that the 'place_id' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.place_id, str)

    def test_user_id(self):
        """
        Test that the 'user_id' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.user_id, str)

    def test_text(self):
        """
        Test that the 'text' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.text, str)
