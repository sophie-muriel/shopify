# models/product.py
from sqlalchemy import Column, Integer, String, Double
from ..db.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    description = Column(String(120))
    price = Column(Double)