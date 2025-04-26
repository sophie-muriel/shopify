# schemas/item.py
from pydantic import BaseModel


class ItemBase(BaseModel):
    date: str
    client_name: str
    client_email: str
    total_price: float
    
class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True
