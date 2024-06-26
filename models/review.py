#!/usr/bin/python3
"""
    This Model Contains the Review Model
"""


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
