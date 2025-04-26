# models/item.py
from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class Receipt(Base):
    __tablename__ = "receipt"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    client_name = Column(String)
    client_email = Column(String)
    total_price = Column(Integer)

