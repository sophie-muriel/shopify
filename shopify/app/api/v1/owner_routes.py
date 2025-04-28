# api/v1/owner_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas.owner_schema import OwnerCreate, OwnerResponse
from ...services.owner_service import create_new_owner, fetch_owner, update_existing_owner, delete_existing_owner
from ...db.session import get_db


router = APIRouter()


@router.post("/owners", response_model=OwnerResponse)
def create_owner_route(owner: OwnerCreate, db: Session = Depends(get_db)):
    """
    Creates a new owner in the database.

    Args:
        owner (OwnerCreate): The OwnerCreate object containing the new owner's details.
        db (Session): The database session.

    Returns:
        OwnerResponse: The created Owner object.

    Raises:
        HTTPException: If there is an integrity error in the database, or any other SQLAlchemy error.
    """
    return create_new_owner(db, owner)


@router.get("/owners/{owner_id}", response_model=OwnerResponse)
def get_owner_route(owner_id: int, db: Session = Depends(get_db)):
    """
    Retrieves the details of an owner by their unique ID.

    Args:
        owner_id (int): The unique ID of the owner to fetch.
        db (Session): The database session.

    Returns:
        OwnerResponse: The Owner object if found.

    Raises:
        HTTPException: If the owner with the given ID is not found (404 Not Found).
    """
    db_owner = fetch_owner(db, owner_id)
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner


@router.put("/owners/{owner_id}", response_model=OwnerResponse)
def update_owner_route(owner_id: int, owner: OwnerCreate, db: Session = Depends(get_db)):
    """
    Updates an owner's information in the database.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to update.
        owner (OwnerCreate): An OwnerCreate object with the new owner's information.

    Returns:
        OwnerResponse: The updated Owner object.

    Raises:
        HTTPException: If there is an integrity error in the database, or any other SQLAlchemy error.
        None: If the owner with the given ID is not found.
    """
    db_owner = update_existing_owner(db, owner_id, owner)
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner


@router.delete("/owners/{owner_id}", response_model=dict)
def delete_owner_route(owner_id: int, db: Session = Depends(get_db)):
    """
    Deletes an owner and all their associated pets from the database.

    Args:
        owner_id (int): The ID of the owner to delete.
        db (Session): The database session.

    Returns:
        dict: A confirmation message indicating the owner was deleted.

    Raises:
        HTTPException: If the owner with the given ID is not found (404 Not Found).
    """
    db_owner = delete_existing_owner(db, owner_id)
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner