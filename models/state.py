#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    # If your storage engine is not DBStorage
    else:
        # getter method
        @property
        def cities(self):
            """Returns list of City objects from storage linked to current State"""
            cities = []
            for city in models.storage.all(City).values:
                if self.id == city.state_id:
                    cities.append(city)
            return cities
