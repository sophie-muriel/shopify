# models/product.py
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from ..db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False, index=True)
    description = Column(String(500))
    price = Column(Numeric(10, 2), nullable=False)

    receipts = relationship("ReceiptProduct", back_populates="product")
