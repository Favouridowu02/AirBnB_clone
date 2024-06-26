#!/usr/bin/python3
"""
    This Model contains the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        This is the city Model
        Attributes:
            state_id: the state id
            name: the name of the city
    """
    state_id = ""
    name = ""
