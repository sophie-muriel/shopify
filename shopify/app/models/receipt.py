# models/receipt.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import date
from ..db.database import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, default=date.today)
    client_name = Column(String(100))
    client_email = Column(String(255), index=True)

    products = relationship("ReceiptProduct", back_populates="receipt")
