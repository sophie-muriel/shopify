# models/receipt.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from ..db.database import Base


class Receipt(Base):
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    client_name = Column(String(40))
    client_email = Column(String(255))

    products = relationship("Receipt_product", back_populates="receipt")
