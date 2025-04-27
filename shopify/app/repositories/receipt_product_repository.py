# repositories/receipt_repository.py
from sqlalchemy.orm import Session
from ..models.receipt_product import Receipt_product
from ..schemas.receipt_product_schema import ReceiptProductCreate


def create_receipt_product(db: Session, receipt_product: ReceiptProductCreate):
    # Create the new receipt product record in the database
    db_receipt_product = Receipt_product(
        receipt_id=receipt_product.receipt_id,
        product_id=receipt_product.product_id,
        quantity=receipt_product.quantity
    )
    db.add(db_receipt_product)
    db.commit()
    db.refresh(db_receipt_product)
    return db_receipt_product


def get_receipt_product(db: Session, receipt_product_id: int):
    return db.query(Receipt_product).filter(Receipt_product.id == receipt_product_id).first()


def delete_receipt_product(db: Session, receipt_product_id: int):
    db_receipt_product = get_receipt_product(db, receipt_product_id)
    if not db_receipt_product:
        return None
    db.delete(db_receipt_product)
    db.commit()
    return {"message": "receipt_product deleted successfully"}
