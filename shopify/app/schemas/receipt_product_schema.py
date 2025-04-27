# schemas/receipt_product_schema.py
from pydantic import BaseModel
from ..schemas.product_schema import ProductResponse


class ReceiptProductBase(BaseModel):
    product_id: int
    quantity: int


class ReceiptProductCreate(ReceiptProductBase):
    pass


class ReceiptProductResponse(BaseModel):
    id: int
    quantity: int
    total_price: float
    product: ProductResponse

    class Config:
        orm_mode = True
