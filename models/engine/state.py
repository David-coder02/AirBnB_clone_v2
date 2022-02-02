#!/usr/bin/python3
"""This is a class for state"""
from os import getenv
from sqlalchemy.orm import relationship 
from sqlalchemy import String, DateTime, Column, ForeignKey
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is a class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Get attribute in case of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
