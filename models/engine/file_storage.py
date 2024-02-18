#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone.
"""

import json
from models import storage  # Add this import statement


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.

        Args:
            cls (class): The class to filter models by.

        Returns:
            dict: A dictionary containing models of the specified class.
                  If cls is None, returns all models.
        """
        if cls:
            filtered_dict = {}
            for key, val in FileStorage.__objects.items():
                if val.__class__ == cls:
                    filtered_dict[key] = val
            return filtered_dict
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the storage dictionary to a file in JSON format.
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Loads the storage dictionary from the file in JSON format.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    FileStorage.__objects[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.

        Args:
            obj: The object to be deleted.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects.pop(key, None)

    def close(self):
        """
        Calls the reload() method for deserializing the JSON file to objects.
        """
        self.reload()
