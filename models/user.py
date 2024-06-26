#!/usr/bin/python3
"""
    This model contains a class User that inherits from BaseModel
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """
        This class represents the Public Class Attributes

        Public Class Attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __int__(self, *args, **kwargs):
        """
            This is the instantialization of the class
        """
        uper().__init__(*args, **kwargs)
