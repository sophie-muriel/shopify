# api/v1/product_routes.py
from ...services.pet_service import create_new_pet, fetch_pet, update_existing_pet, delete_existing_pet, delete_all_pets_for_owner, fetch_all_pets
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...schemas.pet_schema import PetCreate, PetResponse
from ...db.session import get_db

router = APIRouter()


@router.post("/", response_model=PetResponse)
def create_pet_route(item: PetCreate, db: Session = Depends(get_db)):
    """
    Create a new pet in the database.

    Args:
        item (PetCreate): Pet data to be created.
        db (Session): SQLAlchemy session.

    Returns:
        PetResponse: The created pet object.

    Raises:
        HTTPException: If there is an error creating the pet.
    """
    return create_new_pet(db, item)


@router.get("/{pet_id}", response_model=PetResponse)
def get_pet_route(pet_id: int, db: Session = Depends(get_db)):
    """
    Get a pet by its ID.

    Args:
        pet_id (int): The ID of the pet to retrieve.
        db (Session): SQLAlchemy session.

    Returns:
        PetResponse: The retrieved pet object.

    Raises:
        HTTPException: If no pet is found with the provided ID.
    """
    db_pet = fetch_pet(db, pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


@router.get("/owner/{owner_id}/pets", response_model=List[PetResponse])
def get_all_pets_for_owner_route(owner_id: int, db: Session = Depends(get_db)):
    """
    Get all pets for a specific owner.

    Args:
        owner_id (int): The ID of the owner whose pets need to be fetched.
        db (Session): SQLAlchemy session.

    Returns:
        List[PetResponse]: A list of pets associated with the owner.

    Raises:
        HTTPException: If no pets are found for the owner.
    """
    pets = fetch_all_pets(db, owner_id)
    if not pets:
        raise HTTPException(
            status_code=404, detail="No pets found for this owner")
    return pets


@router.put("/{pet_id}", response_model=PetResponse)
def update_pet_route(pet_id: int, pet: PetCreate, db: Session = Depends(get_db)):
    """
    Update an existing pet by its ID.

    Args:
        pet_id (int): The ID of the pet to update.
        pet (PetCreate): The new pet data to update.
        db (Session): SQLAlchemy session.

    Returns:
        PetResponse: The updated pet object.

    Raises:
        HTTPException: If no pet is found with the provided ID or there is an error during the update.
    """
    db_pet = update_existing_pet(db, pet_id, pet)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


@router.delete("/{pet_id}", response_model=dict)
def delete_pet_route(pet_id: int, db: Session = Depends(get_db)):
    """
    Delete a pet by its ID.

    Args:
        pet_id (int): The ID of the pet to delete.
        db (Session): SQLAlchemy session.

    Returns:
        dict: A message confirming the deletion of the pet.

    Raises:
        HTTPException: If no pet is found with the provided ID or there is an error during the deletion.
    """
    db_pet = delete_existing_pet(db, pet_id)
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted successfully"}


@router.delete("/owner/{owner_id}", response_model=dict)
def delete_all_pets_route(owner_id: int, db: Session = Depends(get_db)):
    """
    Delete all pets for a specific owner.

    Args:
        owner_id (int): The ID of the owner for whom all pets need to be deleted.
        db (Session): SQLAlchemy session.

    Returns:
        dict: A message confirming the deletion of all pets for the owner.

    Raises:
        HTTPException: If there is an error deleting the pets or no pets are found for the owner.
    """
    result = delete_all_pets_for_owner(db, owner_id)
    return result
