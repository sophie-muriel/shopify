# schemas/receipt_schema.py
from pydantic import BaseModel
from typing import List
from ..schemas.product_schema import ProductResponse


class ReceiptProductCreate(BaseModel):
    product_id: int
    quantity: int


class ReceiptBase(BaseModel):
    date: str
    client_name: str
    client_email: str


class ReceiptCreate(ReceiptBase):
    products_list: List[ReceiptProductCreate]


class ReceiptResponse(ReceiptBase):
    id: int
    total_price: float
    products: List[ReceiptProductCreate]

    class Config:
        orm_mode = True
