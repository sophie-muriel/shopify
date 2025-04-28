# models/owner.py
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from ..db.database import Base


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    phone = Column(String(10))
    email = Column(String(40), nullable=False, index=True)
    address = Column(String(100))

    pets = relationship("Pet", back_populates="owner")