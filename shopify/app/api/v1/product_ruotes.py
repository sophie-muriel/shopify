# api/v1/product_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import create_new_product, fetch_product, update_existing_product, delete_existing_product
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=ProductResponse)
def create_product_route(item: ProductCreate, db: Session = Depends(get_db)):
    return create_new_product(db, item)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = fetch_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/update/{product_id}", response_model=ProductResponse)
def function_one(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
   db_product = update_existing_product(db, product_id, product)
   if not db_product:
       raise HTTPException(status_code=404, detail="Product not found")
   return db_product


@router.delete("/delete/{product_id}")
def function_two(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_existing_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product