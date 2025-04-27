# services/product_service.py
from sqlalchemy.orm import Session
from app.repositories.product_repository import create_product, get_product, update_product, delete_product
from app.schemas.product import ProductCreate


def create_new_product(db: Session, product: ProductCreate):
    return create_product(db, product)


def fetch_product(db: Session, product_id: int):
    return get_product(db, product_id)


def update_existing_product(db: Session, product_id: int, product: ProductCreate):
   return update_product(db, product_id, product)


def delete_existing_product(db: Session, product_id: int):
    return delete_product(db, product_id)