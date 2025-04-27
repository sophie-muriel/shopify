# models/product.py
from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    description = Column(String(120))
    price = Column(Double)

    receipts = relationship("Receipt_product", back_populates="product")
