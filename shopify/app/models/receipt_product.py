# models/receipt_product.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base
from ..models.product import Product
from ..models.receipt import Receipt


class Receipt_product(Base):
    __tablename__ = "receipt_product"

    id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey(Receipt.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)

    receipt = relationship("Receipt", back_populates="products")
    product = relationship("Product", back_populates="receipts")
