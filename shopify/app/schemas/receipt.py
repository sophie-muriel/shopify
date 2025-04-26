# schemas/receipt.py
from pydantic import BaseModel


class ReceiptBase(BaseModel):
    date: str
    client_name: str
    client_email: str

class ReceiptCreate(ReceiptBase):
    products_list: list


class ReceiptResponse(ReceiptBase):
    id: int
    total_price: float

    class Config:
        orm_mode = True

class ReceiptProductCreate(BaseModel):
    product_id: int
    receipt_id: int