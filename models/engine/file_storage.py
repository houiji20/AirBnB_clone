#!/usr/bin/python3
"""File IO api."""
from json import dump, load
from os.path import exists

class FileStorage():
    """Class for serialization and deserialization of json file."""

    __file_path = "model.json"
    __objects = {}

    def all(self):
        """Retun all objects in memory."""
        return __class__.__objects

    def new(self, obj):
        """Add an object."""
        __class__.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Save objects to file."""
        dict = {}
        with open(__class__.__file_path, 'w') as f:
            for key in __class__.__objects:
                dict[key] = __class__.__objects[key].to_dict()
            dump(dict, f)

    def reload(self):
        """Reload objects from file."""
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        if exists(__class__.__file_path):
            with open(__class__.__file_path, 'r') as f:
                objs = load(f)
            for key in objs:
                __class__.__objects[key] = eval(objs[key]['__class__'])(**objs[key])
