# services/receipt_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.product import Product
from ..repositories.receipt_repository import create_receipt, get_receipt, update_receipt, delete_receipt
from ..repositories.receipt_product_repository import create_receipt_product, get_receipt_product, delete_receipt_product
from ..schemas.receipt_schema import ReceiptCreate, ReceiptProductCreate


def create_new_receipt(db: Session, receipt: ReceiptCreate):
    try:
        db.begin()

        new_receipt = create_receipt(db, receipt)

        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()
            if not db_product:
                raise HTTPException(
                    status_code=404, detail=f"Product with ID {product.product_id} not found")

            receipt_product = ReceiptProductCreate(
                receipt_id=new_receipt.id,
                product_id=product.product_id,
                quantity=product.quantity
            )
            create_receipt_product(db, receipt_product)

        db.commit()

        return new_receipt

    except SQLAlchemyError as e:
        db.rollback()
        raise e


def fetch_receipt(db: Session, receipt_id: int):
    return get_receipt(db, receipt_id)


def delete_existing_receipt(db: Session, receipt_id: int):
    return delete_receipt(db, receipt_id)
