# models/pet.py
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base
from enum import Enum as PyEnum


class SexEnum(PyEnum):
    """
    Enum representing the sex of a pet.

    Attributes:
        male: Represents male sex.
        female: Represents female sex.
    """
    male = "Male"
    female = "Female"


class Pet(Base):
    """
    Represents a pet in the system.

    Attributes:
        id (int): The unique identifier for the pet.
        name (str): The name of the pet. This is a required field.
        species (str): The species of the pet. This is a required field.
        breed (str): The breed of the pet. Optional field.
        sex (SexEnum): The sex of the pet. Can be 'Male' or 'Female'. This is a required field.
        owner_id (int): The unique identifier of the pet's owner. This is a required field.

    Relationships:
        owner (Owner): The owner of the pet. It links to the `Owner` model.
    """
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    species = Column(String(100), nullable=False)
    breed = Column(String(100))
    sex = Column(Enum(SexEnum), nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)

    owner = relationship("Owner", back_populates="pets")
