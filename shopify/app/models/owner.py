# models/owner.py
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from ..db.database import Base


class Owner(Base):
    """
    Represents an owner in the system.

    Attributes:
        id (int): The unique identifier for the owner.
        first_name (str): The first name of the owner. This is a required field.
        last_name (str): The last name of the owner. This is a required field.
        phone (str): The phone number of the owner. Optional field.
        email (str): The email address of the owner. This is a required field.
        address (str): The address of the owner. Optional field.

    Relationships:
        pets (Pet): The pets owned by the owner. It links to the `Pet` model.
  """
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    phone = Column(String(10))
    email = Column(String(40), nullable=False, index=True)
    address = Column(String(100))

    pets = relationship("Pet", back_populates="owner")