#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel):
    """ State class 
    Attributes:
        __tablename__: table name
        name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """get all cities with the current state id
            from file storage
            """
            l = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return (l)
