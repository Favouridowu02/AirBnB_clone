#!/usr/bin/python3
"""
    This Model Contains the Review Model
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
        This is the Review Model

        Public Attributes:
            place_id: the place id
            user_id: the user id
            text: the text
    """
    place_id = ""
    user_id = ""
    text = ""
