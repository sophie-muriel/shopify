# schemas/owner_schema.py
from pydantic import BaseModel


class OwnerBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    address: str


class OwnerCreate(OwnerBase):
    pass


class OwnerResponse(OwnerBase):
    id: int

    class Config:
        orm_mode = True