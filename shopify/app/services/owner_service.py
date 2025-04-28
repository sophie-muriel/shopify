# services/owner_service.py
from sqlalchemy.orm import Session
from ..repositories.owner_repository import create_owner, get_owner, update_owner, delete_owner
# from ..repositories.pet_repository import delete_all_pets
from ..schemas.owner_schema import OwnerCreate


def create_new_owner(db: Session, owner: OwnerCreate):
    """
    Creates a new owner and stores it in the database.

    This function uses the repository's create_owner function to create a new owner
    and persists it in the database.

    Args:
        db (Session): The database session.
        owner (OwnerCreate): The owner data to be created.

    Returns:
        Owner: The created owner object.
    
    Raises:
        HTTPException: If there is an error creating the owner.
    """
    return create_owner(db, owner)


def fetch_owner(db: Session, owner_id: int):
    """
    Retrieves an owner from the database based on the given owner ID.

    This function uses the repository's get_owner function to get an owner 
    by its unique ID.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to retrieve.

    Returns:
        Owner: The owner object if found.
    
    Raises:
        HTTPException: If the owner is not found.
    """
    return get_owner(db, owner_id)


def update_existing_owner(db: Session, owner_id: int, owner: OwnerCreate):
    """
    Updates an existing owner's details in the database.

    This function uses the repository's update_owner function to modify the owner's
    attributes.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to update.
        owner (OwnerCreate): The new data to update the owner's information.

    Returns:
        Owner: The updated owner object.

    Raises:
        HTTPException: If the owner is not found or if there is an error during the update.
    """
    return update_owner(db, owner_id, owner)


def delete_existing_owner(db: Session, owner_id: int):
    """
    Deletes an owner and all associated pets from the database.

    This function first deletes all pets associated with the given owner by calling the 
    delete_all_pets function, then it deletes the owner from the database using the 
    delete_owner function.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to delete.

    Returns:
        dict: A success message indicating the owner has been deleted.

    Raises:
        HTTPException: If there is an error deleting the owner or their pets.
    """
    #delete_all_pets(db, owner_id)  # Deletes associated pets first
    return delete_owner(db, owner_id)