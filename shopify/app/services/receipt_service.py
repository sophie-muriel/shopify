# services/receipt_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.product import Product
from ..models.receipt_product import Receipt_product
from ..repositories.receipt_repository import create_receipt, get_receipt, update_receipt, delete_receipt
from ..repositories.receipt_product_repository import create_receipt_product, get_receipt_product, delete_receipt_product
from ..schemas.receipt_schema import ReceiptCreate, ReceiptResponse
from ..schemas.receipt_product_schema import ReceiptProductResponse


def create_new_receipt(db: Session, receipt: ReceiptCreate):
    try:
        db.begin()
        new_receipt = create_receipt(db, receipt)

        receipt_products = []
        for product in receipt.products_list:
            db_product = db.query(Product).filter(
                Product.id == product.product_id).first()
            if not db_product:
                raise HTTPException(
                    status_code=404, detail=f"Product with ID {product.product_id} not found")

            receipt_product = Receipt_product(
                receipt_id=new_receipt.id,
                product_id=product.product_id,
                quantity=product.quantity
            )
            new_receipt.products.append(receipt_product)

        db.commit()
        db.refresh(new_receipt)

        for receipt_product in new_receipt.products:
            db_product = db.query(Product).filter(
                Product.id == receipt_product.product_id).first()
            if db_product:
                receipt_product_response = ReceiptProductResponse(
                    id=receipt_product.id,
                    receipt_id=receipt_product.receipt_id,
                    product_id=receipt_product.product_id,
                    quantity=receipt_product.quantity,
                    product_name=db_product.product_name,
                    description=db_product.description,
                    price=db_product.price
                )
                receipt_products.append(receipt_product_response)

        total_price = calculate_total_price(db, new_receipt.id)
        setattr(new_receipt, 'total_price', total_price)

        return ReceiptResponse(
            id=new_receipt.id,
            date=new_receipt.date,
            client_name=new_receipt.client_name,
            client_email=new_receipt.client_email,
            total_price=total_price,
            products=receipt_products
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def fetch_receipt(db: Session, receipt_id: int):
    receipt = get_receipt(db, receipt_id)
    if not receipt:
        return None

    receipt_products = []
    for receipt_product in receipt.products:
        db_product = db.query(Product).filter(
            Product.id == receipt_product.product_id).first()
        if db_product:
            receipt_product_response = ReceiptProductResponse(
                id=receipt_product.id,
                receipt_id=receipt_product.receipt_id,
                product_id=receipt_product.product_id,
                quantity=receipt_product.quantity,
                product_name=db_product.product_name,
                description=db_product.description,
                price=db_product.price
            )
            receipt_products.append(receipt_product_response)

    total_price = calculate_total_price(db, receipt_id)

    return ReceiptResponse(
        id=receipt.id,
        date=receipt.date,
        client_name=receipt.client_name,
        client_email=receipt.client_email,
        total_price=total_price,
        products=receipt_products
    )


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
