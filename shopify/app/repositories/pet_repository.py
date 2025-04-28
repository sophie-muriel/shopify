# repositories/pet_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models.pet import Pet
from ..models.owner import Owner
from ..schemas.pet_schema import PetCreate


def create_pet(db: Session, pet: PetCreate):
    """
    Creates a new pet in the database.

    Args:
        db (Session): The SQLAlchemy session object.
        pet (PetCreate): The pet data to be added to the database.

    Returns:
        Pet: The created pet object.

    Raises:
        Exception: If there is an error creating the pet.
    """
    try:
        db_owner = db.query(Owner).filter(Owner.id == pet.owner_id).first()
        if not db_owner:
            raise HTTPException(status_code=404, detail="Owner not found.")

        sex_value = pet.sex.value

        db_pet = Pet(
            name=pet.name,
            species=pet.species,
            breed=pet.breed,
            sex=sex_value,
            owner_id=pet.owner_id
        )

        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error creating pet")


def get_pet(db: Session, pet_id: int):
    """
    Retrieves a pet by its ID from the database.

    Args:
        db (Session): The SQLAlchemy session object.
        pet_id (int): The ID of the pet to retrieve.

    Returns:
        Pet: The pet object if found, None otherwise.
    """
    return db.query(Pet).filter(Pet.id == pet_id).first()


def get_all_pets(db: Session, owner_id: int):
    """
    Retrieves all pets for a given owner from the database.

    Args:
        db (Session): The SQLAlchemy session object.
        owner_id (int): The ID of the owner whose pets are to be retrieved.

    Returns:
        List[Pet]: A list of pets owned by the given owner.

    Raises:
        HTTPException: If no pets are found for the given owner.
    """
    pets = db.query(Pet).filter(Pet.owner_id == owner_id).all()
    if not pets:
        raise HTTPException(
            status_code=404, detail="No pets found for this owner.")
    return pets


def update_pet(db: Session, pet_id: int, pet: PetCreate):
    """
    Updates an existing pet in the database.

    Args:
        db (Session): The SQLAlchemy session object.
        pet_id (int): The ID of the pet to update.
        pet (PetCreate): The new pet data to update the pet with.

    Returns:
        Pet: The updated pet object, or None if the pet was not found.

    Raises:
        Exception: If there is an error updating the pet.
    """
    db_pet = get_pet(db, pet_id)
    if not db_pet:
        return None

    db_owner = db.query(Owner).filter(Owner.id == pet.owner_id).first()
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found.")

    db_pet.name = pet.name
    db_pet.species = pet.species
    db_pet.breed = pet.breed
    db_pet.sex = pet.sex
    db_pet.owner_id = pet.owner_id

    try:
        db.commit()
        db.refresh(db_pet)
        return db_pet
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error updating pet")


def delete_pet(db: Session, pet_id: int):
    """
    Deletes a pet by its ID from the database.

    Args:
        db (Session): The SQLAlchemy session object.
        pet_id (int): The ID of the pet to delete.

    Returns:
        dict: A dictionary with a success message, or None if the pet was not found.

    Raises:
        Exception: If there is an error deleting the pet.
    """
    db_pet = get_pet(db, pet_id)
    if not db_pet:
        return None
    try:
        db.delete(db_pet)
        db.commit()
        return {"message": "Pet deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error deleting pet")


def delete_all_pets(db: Session, owner_id: int):
    """
    Deletes all pets associated with a given owner.

    Args:
        db (Session): The SQLAlchemy session object.
        owner_id (int): The ID of the owner whose pets need to be deleted.

    Returns:
        dict: A dictionary with a success message or an error message if no pets were found.

    Raises:
        HTTPException: If no pets are found for the given owner.
        Exception: If there is an error deleting the pets.
    """
    try:
        pets_to_delete = db.query(Pet).filter(Pet.owner_id == owner_id).all()

        if not pets_to_delete:
            raise HTTPException(
                status_code=404, detail="No pets found for this owner.")

        for pet in pets_to_delete:
            db.delete(pet)

        db.commit()
        return {"message": "All pets deleted successfully for owner with id {owner_id}"}
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error deleting pets")
