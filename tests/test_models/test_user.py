#!/usr/bin/python
"""
Test module for the User model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """
    Test class for User model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test that the 'first_name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.first_name, str)

    def test_last_name(self):
        """
        Test that the 'last_name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.last_name, str)

    def test_email(self):
        """
        Test that the 'email' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.email, str)

    def test_password(self):
        """
        Test that the 'password' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.password, str)
