#!/usr/bin/python3
"""
    This Model contains the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        This is the Place Class:

        Public Attributes:
            city_id: the city id
            user_id: the user id
            name: the name of the place
            description: the description of the place
            number_rooms: the rooms numbers
            number_bathrooms: the number of bathrooms
            max_guest: the maximum guests numbers
            price_by_night: the price for night
            latitude: the latitude
            longitude: the longitude
            amenity_ids: the amenity id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
