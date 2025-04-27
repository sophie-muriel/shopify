# services/receipt_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..repositories.receipt_repository import create_receipt, get_receipt, update_receipt, delete_receipt
from ..schemas.receipt_schema import ReceiptCreate, ReceiptResponse
from ..schemas.receipt_product_schema import ReceiptProductResponse
from ..schemas.product_schema import ProductResponse
from sqlalchemy.exc import SQLAlchemyError


def create_new_receipt(db: Session, receipt: ReceiptCreate):
    try:
        new_receipt = create_receipt(db, receipt)
        receipt_products = [
            ReceiptProductResponse(
                id=receipt_product.id,
                quantity=receipt_product.quantity,
                total_price=receipt_product.quantity * receipt_product.product.price,
                product=ProductResponse(
                    id=receipt_product.product.id,
                    product_name=receipt_product.product.product_name,
                    description=receipt_product.product.description,
                    price=float(receipt_product.product.price)
                )
            )
            for receipt_product in new_receipt.products
        ]
        return ReceiptResponse(
            id=new_receipt.id,
            date=new_receipt.date,
            client_name=new_receipt.client_name,
            client_email=new_receipt.client_email,
            total_price=sum(p.total_price for p in receipt_products),
            products=receipt_products
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Database error occurred: {str(e)}")


def fetch_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    receipt_products = [
        ReceiptProductResponse(
            id=receipt_product.id,
            quantity=receipt_product.quantity,
            total_price=receipt_product.quantity * receipt_product.product.price,
            product=ProductResponse(
                id=receipt_product.product.id,
                product_name=receipt_product.product.product_name,
                description=receipt_product.product.description,
                price=float(receipt_product.product.price)
            )
        )
        for receipt_product in receipt.products
    ]
    return ReceiptResponse(
        id=receipt.id,
        date=receipt.date,
        client_name=receipt.client_name,
        client_email=receipt.client_email,
        total_price=sum(p.total_price for p in receipt_products),
        products=receipt_products
    )


def update_existing_receipt(db: Session, receipt_id: int, receipt: ReceiptCreate):
    updated_receipt = update_receipt(db, receipt_id, receipt)
    if not updated_receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    receipt_products = [
        ReceiptProductResponse(
            id=receipt_product.id,
            quantity=receipt_product.quantity,
            total_price=receipt_product.quantity * receipt_product.product.price,
            product=ProductResponse(
                id=receipt_product.product.id,
                product_name=receipt_product.product.product_name,
                description=receipt_product.product.description,
                price=float(receipt_product.product.price)
            )
        )
        for receipt_product in updated_receipt.products
    ]
    return ReceiptResponse(
        id=updated_receipt.id,
        date=updated_receipt.date,
        client_name=updated_receipt.client_name,
        client_email=updated_receipt.client_email,
        total_price=sum(p.total_price for p in receipt_products),
        products=receipt_products
    )


def delete_existing_receipt(db: Session, receipt_id: int):
    result = delete_receipt(db, receipt_id)
    if not result:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return result
