# api/v1/receipt_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas.receipt_schema import ReceiptCreate, ReceiptResponse
from ...services.receipt_service import create_new_receipt, fetch_receipt, delete_existing_receipt
from ...db.session import get_db


router = APIRouter()


@router.post("/", response_model=ReceiptResponse)
def create_receipt_route(item: ReceiptCreate, db: Session = Depends(get_db)):
    return create_new_receipt(db, item)


@router.get("/{receipt_id}", response_model=ReceiptResponse)
def get_receipt_route(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = fetch_receipt(db, receipt_id)
    if not db_receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return db_receipt


@router.delete("/{receipt_id}", response_model=dict)
def delete_receipt_route(receipt_id: int, db: Session = Depends(get_db)):
    db_receipt = delete_existing_receipt(db, receipt_id)
    if not db_receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return db_receipt
