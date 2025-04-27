# schemas/receipt_product_schema.py
from pydantic import BaseModel


class ReceiptProductBase(BaseModel):
    receipt_id: int
    product_id: int
    quantity: int


class ReceiptProductCreate(ReceiptProductBase):
    pass


class ReceiptProductResponse(ReceiptProductBase):
    id: int

    class Config:
        orm_mode = True
