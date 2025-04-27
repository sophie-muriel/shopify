# models/receipt_product.py
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from ..db.database import Base


class ReceiptProduct(Base):
    __tablename__ = "receipt_products"
    __table_args__ = (CheckConstraint(
        'quantity > 0', name='positive_quantity'),)

    id = Column(Integer, primary_key=True, index=True)
    receipt_id = Column(Integer, ForeignKey('receipts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

    receipt = relationship("Receipt", back_populates="products")
    product = relationship("Product", back_populates="receipts")
