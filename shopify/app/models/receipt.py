# models/item.py
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Receipt(Base):
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(10))
    client_name = Column(String(40))
    client_email = Column(String(30))
    total_price = Column(Integer)

