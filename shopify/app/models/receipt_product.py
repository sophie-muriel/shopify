# models/receipt_product.py
from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base
from app.models.product import Product
from app.models.receipt import Receipt


class Receipt_product(Base):
    __tablename__ = "receipt_product"

    id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey(Receipt.id))
    product_id = Column(Integer, ForeignKey(Product.id))