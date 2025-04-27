# repositories/receipt_product_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.receipt_product import ReceiptProduct
from ..schemas.receipt_product_schema import ReceiptProductCreate


def create_receipt_product(db: Session, receipt_product: ReceiptProductCreate, receipt_id: int):
    try:
        db_receipt_product = ReceiptProduct(
            receipt_id=receipt_id,
            product_id=receipt_product.product_id,
            quantity=receipt_product.quantity
        )
        db.add(db_receipt_product)
        db.commit()
        db.refresh(db_receipt_product)
        return db_receipt_product
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error creating receipt product")


def get_receipt_product(db: Session, receipt_product_id: int):
    return db.query(ReceiptProduct).filter(ReceiptProduct.id == receipt_product_id).first()


def delete_receipt_product(db: Session, receipt_product_id: int):
    try:
        db_receipt_product = get_receipt_product(db, receipt_product_id)
        if not db_receipt_product:
            return None
        db.delete(db_receipt_product)
        db.commit()
        return {"message": "Receipt_product deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise Exception("Error deleting receipt product")
