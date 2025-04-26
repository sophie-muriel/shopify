# schemas/product.py
from pydantic import BaseModel


class ProductBase(BaseModel):
    product_name: str
    description: str
    client_email: str
    price: float

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True