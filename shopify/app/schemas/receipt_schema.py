# schemas/receipt_schema.py
from pydantic import BaseModel
from typing import List
from datetime import date
from ..schemas.product_schema import ProductResponse
from ..schemas.receipt_product_schema import ReceiptProductResponse


class ReceiptProductCreate(BaseModel):
    product_id: int
    quantity: int


class ReceiptBase(BaseModel):
    date: date
    client_name: str
    client_email: str


class ReceiptCreate(ReceiptBase):
    products_list: List[ReceiptProductCreate]


class ReceiptResponse(ReceiptBase):
    id: int
    total_price: float
    products: List[ReceiptProductResponse]

    class Config:
        orm_mode = True
