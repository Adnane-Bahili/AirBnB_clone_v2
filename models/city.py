#!/usr/bin/python3
"""defines the 'City' class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class City(BaseModel, Base):
    """represents a city for a MySQL database
    inherits from SQLAlchemy Base and links to the MySQL table cities
    attributes:
        __tablename__ (str): MySQL table's name whre to store Cities
        name (sqlalchemy String): City name
        state_id (sqlalchemy String): City state id
    """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place', cascade="all,delete", backref="cities")
    else:
        name = ""
        state_id = ""
