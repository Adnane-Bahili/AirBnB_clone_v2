#!/usr/bin/python3
"""'FileStorage' class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


class FileStorage:
    """manages storage of HBNB models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary of instantiated objects in __objects
        when a cls is given, returns a dictionary of objects of that type
        when It's not, returns the __objects dictionary
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for key, val in self.__objects.items():
                if type(val) == cls:
                    cls_dict[key] = val
            return cls_dict
        return self.__objects

    def new(self, obj):
        """adds objects"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """saves dictionary to file"""
        dict_obj = {obj: self.__objects[obj].to_dict()
                    for obj in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as fl:
            json.dump(dict_obj, fl)

    def reload(self):
        """loads dictionary from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as fl:
                for obj in json.load(fl).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """checks if an object exists and delets it"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Reload method"""
        self.reload()
