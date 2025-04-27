# schemas/receipt_product_schema.py
from pydantic import BaseModel


class ReceiptProductBase(BaseModel):
    product_id: int
    quantity: int


class ReceiptProductCreate(ReceiptProductBase):
    pass


class ReceiptProductResponse(ReceiptProductBase):
    product_name: str
    description: str
    price: float

    class Config:
        orm_mode = True
