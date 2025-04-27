# schemas/owner_schema.py
from pydantic import BaseModel, EmailStr, constr


class OwnerBase(BaseModel):
    first_name: str
    last_name: str
    phone: str = constr(min_length=10, max_length=10)
    email: EmailStr
    address: str


class OwnerCreate(OwnerBase):
    pass


class OwnerResponse(OwnerBase):
    id: int

    class Config:
        orm_mode = True