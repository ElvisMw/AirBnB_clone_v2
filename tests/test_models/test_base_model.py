#!/usr/bin/python
"""
Test module for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    Base test class for BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        self.model_instance = None

    def setUp(self):
        """
        Set up resources for tests.
        """
        self.model_instance = self.value()

    def tearDown(self):
        """
        Clean up resources after tests.
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """
        Test default constructor.
        """
        i = self.model_instance
        self.assertIsInstance(i, self.value)

    def test_kwargs(self):
        """
        Test constructor with kwargs.
        """
        i = self.model_instance
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Test constructor with kwargs containing an int.
        """
        i = self.model_instance
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Testing save.
        """
        i = self.model_instance
        i.save()
        key = f'{self.name}.{i.id}'
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Test str method.
        """
        i = self.model_instance
        expected_str = f'[{self.name}] ({i.id}) {i.__dict__}'
        self.assertEqual(str(i), expected_str)

    def test_todict(self):
        """
        Test to_dict method.
        """
        i = self.model_instance
        self.assertEqual(i.to_dict(), i.to_dict())

    def test_kwargs_none(self):
        """
        Test constructor with kwargs containing None.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """
        Test constructor with kwargs containing one item.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)

    def test_id(self):
        """
        Test id attribute.
        """
        new = self.model_instance
        self.assertIsInstance(new.id, str)

    def test_created_at(self):
        """
        Test created_at attribute.
        """
        new = self.model_instance
        self.assertIsInstance(new.created_at, datetime.datetime)

    def test_updated_at(self):
        """
        Test updated_at attribute.
        """
        new = self.model_instance
        self.assertIsInstance(new.updated_at, datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
