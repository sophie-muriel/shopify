# schemas/pet_schema.py
from pydantic import BaseModel, Field, conint, constr
from ..commons.enums import SexEnum


class PetBase(BaseModel):
    """
    Base schema for creating or updating a pet.

    Attributes:
        name (str): The name of the pet. This is a required field and cannot be empty.
        species (str): The species of the pet. This is a required field and cannot be empty.
        breed (str | None): The breed of the pet. This field is optional and can be None.
        sex (SexEnum): The sex of the pet, must be either 'male' or 'female'.
        owner_id (int): The unique identifier of the pet's owner. This field is required.
    """
    name: str = constr(min_length=1, max_length=100)
    species: str = constr(min_length=1, max_length=100)
    breed: str | None = Field(default=None, max_length=100)
    sex: SexEnum
    owner_id: int = conint(ge=1)


class PetCreate(PetBase):
    pass


class PetResponse(PetBase):
    id: int

    class Config:
        orm_mode = True
