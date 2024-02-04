#!/usr/bin/python
"""
Test module for the State model.
"""

from tests.test_models.test_basemodel import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """
    Test class for State model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """
        Test that the 'name' attribute is a string.
        """
        new = self.model_instance
        self.assertIsInstance(new.name, str)
