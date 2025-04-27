# repositories/product_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.product import Product
from ..schemas.product_schema import ProductCreate


def create_product(db: Session, product: ProductCreate):
    try:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error creating product")


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db_product.product_name = product.product_name
    db_product.description = product.description
    db_product.price = product.price
    try:
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error updating product")


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    try:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error deleting product")
