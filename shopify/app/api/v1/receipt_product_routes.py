# api/v1/receipt_product_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas.receipt_product_schema import ReceiptProductCreate, ReceiptProductResponse
from ...services.receipt_product_service import create_new_receipt_product, fetch_receipt_product, delete_existing_receipt_product
from ...db.session import get_db


router = APIRouter()


@router.post("/", response_model=ReceiptProductResponse)
def create_receipt_product_route(item: ReceiptProductCreate, db: Session = Depends(get_db)):
    return create_new_receipt_product(db, item)


@router.get("/{receipt_product_id}", response_model=ReceiptProductResponse)
def get_receipt_product_route(receipt_product_id: int, db: Session = Depends(get_db)):
    db_receipt_product = fetch_receipt_product(db, receipt_product_id)
    if not db_receipt_product:
        raise HTTPException(
            status_code=404, detail="Receipt product not found")
    return db_receipt_product


@router.delete("/{receipt_product_id}", response_model=dict)
def delete_receipt_product_route(receipt_product_id: int, db: Session = Depends(get_db)):
    db_receipt_product = delete_existing_receipt_product(
        db, receipt_product_id)
    if not db_receipt_product:
        raise HTTPException(
            status_code=404, detail="Receipt product not found")
    return db_receipt_product
