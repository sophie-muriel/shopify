# schemas/owner_schema.py
from pydantic import BaseModel, EmailStr, constr


class OwnerBase(BaseModel):
    """
    Base schema for creating or updating an owner.

    Attributes:
        first_name (str): The first name of the owner. This is a required field and cannot be empty.
        last_name (str): The last name of the owner. This is a required field and cannot be empty.
        phone (str): The phone number of the owner. It must be exactly 10 characters long.
        email (EmailStr): The email address of the owner. This is a required field and must follow a valid email format.
        address (str | None): The address of the owner. This field is optional and can be None.
  """
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