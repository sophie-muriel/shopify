# schemas/receipt.py
from pydantic import BaseModel


class ReceiptBase(BaseModel):
    date: str
    client_name: str
    client_email: str

class ReceiptCreate(ReceiptBase):
    pass


class Receiptponse(ReceiptBase):
    id: int

    class Config:
        orm_mode = True
