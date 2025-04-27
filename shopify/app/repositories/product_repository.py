# repositories/product_repository.py
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: ProductCreate):
   db_product = get_product(db, product_id)
   if not db_product:
       return None
   db_product.product_name = product.product_name
   db_product.description = product.description
   db_product.price = product.price
   db.commit()
   db.refresh(db_product)
   return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return {"message": "product deleted successfully"}