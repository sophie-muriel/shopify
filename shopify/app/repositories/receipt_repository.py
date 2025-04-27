# repositories/receipt_repository.py
from sqlalchemy.orm import Session
from ..models.receipt import Receipt
from ..schemas.receipt import ReceiptCreate


def create_receipt(db: Session, receipt: ReceiptCreate):
    db_receipt = Receipt(**receipt.dict())
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt


def get_receipt(db: Session, receipt_id: int):
    return db.query(Receipt).filter(Receipt.id == receipt_id).first()


def update_receipt(db: Session, receipt_id: int, receipt: ReceiptCreate):
   db_receipt = get_receipt(db, receipt_id)
   if not db_receipt:
       return None
   db_receipt.date = receipt.date
   db_receipt.client_name = receipt.client_name
   db_receipt.client_email = receipt.client_email
   db.commit()
   db.refresh(db_receipt)
   return db_receipt


def delete_receipt(db: Session, receipt_id: int):
    db_receipt = get_receipt(db, receipt_id)
    if not db_receipt:
        return None
    db.delete(db_receipt)
    db.commit()
    return {"message": "receipt deleted successfully"}
