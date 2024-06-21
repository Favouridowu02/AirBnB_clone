#!/usr/bin/python3
"""
    This Module Contains the FileStorage Class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
        This Class Serializes intances to a JSON file and deserializes
        JSON file instances

        Class Methods:
            all: Returns the object
            new: updates the dictionary id
            save: Serializes, or converts Python objects into JSON strings
            reload: Deserializes, or converts JSON strings into Python
                    objects.

        Class Attributes:
            file_path: a private attribute that stores the file path as a
                       string
            objects: a private attribute that stores all objects as a json
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        """
            returns all the __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects to the obj with key <obj class name>.id
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as filename:
            json.dump(obj_dict, filename)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as filename:
                new_obj = json.load(filename)
            for key, value in new_obj.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
