# schemas/receipt.py
from pydantic import BaseModel
from typing import List

class ReceiptProductCreate(BaseModel):
    receipt_id: int
    product_id: int
    quantity: int


class ReceiptBase(BaseModel):
    date: str
    client_name: str
    client_email: str


class ReceiptCreate(ReceiptBase):
    products_list: List['ReceiptProductCreate']


class ReceiptResponse(ReceiptBase):
    id: int
    total_price: float

    class Config:
        orm_mode = True

    