# services/receipt_product_service.py
from sqlalchemy.orm import Session
from ..repositories.receipt_product_repository import create_receipt_product, get_receipt_product, delete_receipt_product
from ..schemas.receipt_product_schema import ReceiptProductCreate, ReceiptProductResponse


def create_new_receipt_product(db: Session, receipt_product: ReceiptProductCreate, receipt_id: int):
    created_receipt_product = create_receipt_product(
        db, receipt_product, receipt_id)
    return ReceiptProductResponse.from_orm(created_receipt_product)


def fetch_receipt_product(db: Session, receipt_product_id: int):
    db_receipt_product = get_receipt_product(db, receipt_product_id)
    if not db_receipt_product:
        raise Exception(
            f"Receipt product with id {receipt_product_id} not found")
    return ReceiptProductResponse.from_orm(db_receipt_product)


def delete_existing_receipt_product(db: Session, receipt_product_id: int):
    return delete_receipt_product(db, receipt_product_id)
