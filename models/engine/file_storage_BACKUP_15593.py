#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
<<<<<<< Updated upstream
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_dict[key] = value
            return filtered_dict
=======
        """returns a dictionary of instantiated objects in __objects
        wjen a 'cls' is specified, returns a dictionary of objects of that type
        If It's not, returns the __objects dictionary
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
    def delete(self, obj=None):
        """If a given object exists,Deletes it from '__objects'"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass
>>>>>>> Stashed changes

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
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
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside.
        If obj is None, the method should not do anything."""

        if obj is None:
            return

        # Search for the object's key in the dictionary
        key_to_delete = None
        for key, value in self.__objects.items():
            if value == obj:
                key_to_delete = key
                break

        # If the object's key is found, delete it from the dictionary
        if key_to_delete:
            del (self.__objects[key_to_delete])
            self.save()