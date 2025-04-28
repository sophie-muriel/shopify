# services/pet_service.py
from sqlalchemy.orm import Session
from ..repositories.pet_repository import create_pet, get_pet, get_all_pets, update_pet, delete_pet, delete_all_pets
from ..schemas.pet_schema import PetCreate


def create_new_pet(db: Session, pet: PetCreate):
    """
    Creates a new pet by calling the create_pet function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        pet (PetCreate): The pet data to be added.

    Returns:
        Pet: The created pet object.
    """
    return create_pet(db, pet)


def fetch_pet(db: Session, pet_id: int):
    """
    Retrieves a pet by its ID by calling the get_pet function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        pet_id (int): The ID of the pet to retrieve.

    Returns:
        Pet: The pet object if found, None otherwise.
    """
    return get_pet(db, pet_id)


def fetch_all_pets(db: Session, owner_id: int):
    """
    Retrieves all pets for a specific owner by calling the get_all_pets function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        owner_id (int): The owner ID for which pets need to be fetched.

    Returns:
        List[Pet]: A list of pets associated with the given owner.
    """
    return get_all_pets(db, owner_id)


def update_existing_pet(db: Session, pet_id: int, pet: PetCreate):
    """
    Updates an existing pet by calling the update_pet function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        pet_id (int): The ID of the pet to update.
        pet (PetCreate): The new pet data.

    Returns:
        Pet: The updated pet object if successful, None if the pet was not found.
    """
    return update_pet(db, pet_id, pet)


def delete_existing_pet(db: Session, pet_id: int):
    """
    Deletes an existing pet by calling the delete_pet function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        pet_id (int): The ID of the pet to delete.

    Returns:
        dict: A dictionary with a success message or None if the pet was not found.
    """
    return delete_pet(db, pet_id)


def delete_all_pets_for_owner(db: Session, owner_id: int):
    """
    Deletes all pets for a specific owner by calling the delete_all_pets function from the repository.

    Args:
        db (Session): The SQLAlchemy session.
        owner_id (int): The owner ID for which pets need to be deleted.

    Returns:
        dict: A message indicating the successful deletion of all pets for the owner.
    """
    return delete_all_pets(db, owner_id)
