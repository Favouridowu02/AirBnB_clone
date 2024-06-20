#!/usr/bin/python3
"""
    This Module contains a Base Model
"""
import uuid
from datetime import datetime, date, time, timezone


class BaseModel:
    """
        This class is the base model
    """
    def __init__(self):
        """
            This class sets up the public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Outputs the class in a formated way
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                str(self.__dict__)))

    def save(self):
        """
            This Method updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        dic = {}
        for key, value in self.__dict__.items():
            dic[key] = value
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat(sep='T', timespec='auto')
        dic["created_at"] = self.created_at.isoformat(sep='T', timespec='auto')

        return dic
