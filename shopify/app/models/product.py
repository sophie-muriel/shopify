# models/product.py
from sqlalchemy import Column, Integer, String, Boolean, Double
from db.database import Base


class Receipt(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    description = Column(String(120))
    total_price = Column(Double)