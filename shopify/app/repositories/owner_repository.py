# repositories/owner_repository.py
# repositories/owner_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..models.owner import Owner
from ..schemas.owner_schema import OwnerCreate
from fastapi import HTTPException

def create_owner(db: Session, owner: OwnerCreate):
    """
    Creates a new owner in the database.

    Args:
        db (Session): The database session.
        owner (OwnerCreate): An OwnerCreate object with the owner's information.

    Returns:
        Owner: The newly created Owner object, with its auto-generated id.

    Raises:
        HTTPException: If there is an integrity error in the database, or any other SQLAlchemy error.
    """
    try:
        db_owner = Owner(**owner.dict())
        db.add(db_owner)
        db.commit()
        db.refresh(db_owner)
        return db_owner
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating owner: {str(e)}")


def get_owner(db: Session, owner_id: int):
    """
    Retrieves an owner from the database by its ID.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to query.

    Returns:
        Owner: The Owner object if found in the database.

    Raises:
        HTTPException: If the owner is not found in the database, a 404 exception is raised.
    """
    owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner


def update_owner(db: Session, owner_id: int, owner: OwnerCreate):
    """
    Updates an owner's information in the database.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to update.
        owner (OwnerCreate): An OwnerCreate object with the new owner's information.

    Returns:
        Owner: The updated Owner object.

    Raises:
        HTTPException: If there is an integrity error in the database, or any other SQLAlchemy error.
        None: If the owner with the given ID is not found.
    """
    db_owner = get_owner(db, owner_id)
    if not db_owner:
        return None
    db_owner.first_name = owner.first_name
    db_owner.last_name = owner.last_name
    db_owner.phone = owner.phone
    db_owner.email = owner.email
    db_owner.address = owner.address
    try:
        db.commit()
        db.refresh(db_owner)
        return db_owner
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating owner: {str(e)}")


def delete_owner(db: Session, owner_id: int):
    """
    Deletes an owner from the database.

    Args:
        db (Session): The database session.
        owner_id (int): The ID of the owner to delete.

    Returns:
        dict: A dictionary with a success message if the owner was successfully deleted.

    Raises:
        HTTPException: If there is a SQLAlchemy error when attempting to delete the owner.
        None: If the owner with the given ID is not found.
    """
    db_owner = get_owner(db, owner_id)
    if not db_owner:
        return None
    try:
        db.delete(db_owner)
        db.commit()
        return {"message": "Owner deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting owner: {str(e)}")
