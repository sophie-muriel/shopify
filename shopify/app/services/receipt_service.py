# services/receipt_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.product import Product
from ..models.receipt_product import Receipt_product
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
            create_receipt_product(db, product, new_receipt.id)

        db.commit()
        db.refresh(new_receipt)

        total_price = calculate_total_price(db, new_receipt.id)
        setattr(new_receipt, 'total_price', total_price)

        return new_receipt
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def fetch_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)
    if not receipt:
        return None

    total_price = calculate_total_price(db, receipt_id)
    setattr(receipt, 'total_price', total_price)
    return receipt


def delete_existing_receipt(db: Session, receipt_id: int):
    return delete_receipt(db, receipt_id)


def calculate_total_price(db: Session, receipt_id: int):
    receipt_products = db.query(Receipt_product).filter(
        Receipt_product.receipt_id == receipt_id).all()
    total = 0.0

    for receipt_product in receipt_products:
        product = db.query(Product).filter(
            Product.id == receipt_product.product_id).first()
        if product:
            total += product.price * receipt_product.quantity

    return total
