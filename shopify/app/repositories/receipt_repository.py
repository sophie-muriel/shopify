# repositories/receipt_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models.receipt import Receipt
from ..models.receipt_product import ReceiptProduct
from ..schemas.receipt_schema import ReceiptCreate
from ..models.product import Product


def create_receipt(db: Session, receipt: ReceiptCreate):
    try:
        db_receipt = Receipt(
            date=receipt.date,
            client_name=receipt.client_name,
            client_email=receipt.client_email
        )

        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()
            if not db_product:
                raise HTTPException(
                    status_code=404, detail=f"Product with ID {product.product_id} not found.")

        db.add(db_receipt)
        db.flush()

        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()

            db_receipt_product = ReceiptProduct(
                receipt_id=db_receipt.id,
                product_id=db_product.id,
                quantity=product.quantity
            )
            db.add(db_receipt_product)

        db.commit()
        db.refresh(db_receipt)
        return db_receipt

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error creating receipt: {str(e)}")
    except HTTPException as e:
        db.rollback()
        raise e


def get_receipt(db: Session, receipt_id: int):
    receipt = db.query(Receipt).filter(Receipt.id == receipt_id).first()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found.")
    return receipt


def update_receipt(db: Session, receipt_id: int, receipt: ReceiptCreate):
    db_receipt = get_receipt(db, receipt_id)
    if not db_receipt:
        return None

    try:
        db_receipt.date = receipt.date
        db_receipt.client_name = receipt.client_name
        db_receipt.client_email = receipt.client_email

        db.query(ReceiptProduct).filter(
            ReceiptProduct.receipt_id == receipt_id).delete()

        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()
            if not db_product:
                raise HTTPException(
                    status_code=404, detail=f"Product with ID {product.product_id} not found.")

        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()

            db_receipt_product = ReceiptProduct(
                receipt_id=db_receipt.id,
                product_id=db_product.id,
                quantity=product.quantity
            )
            db.add(db_receipt_product)

        db.commit()
        db.refresh(db_receipt)
        return db_receipt

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error updating receipt: {str(e)}")
    except HTTPException as e:
        db.rollback()
        raise e


def delete_receipt(db: Session, receipt_id: int):
    db_receipt = get_receipt(db, receipt_id)
    if not db_receipt:
        return None
    try:
        db.delete(db_receipt)
        db.commit()
        return {"message": "Receipt deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error deleting receipt: {str(e)}")
