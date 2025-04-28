# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

from .api.v1 import owner_routes
from .api.v1 import pet_routes

DATABASE_URL = os.getenv(
    "DATABASE_URL", ""
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI(
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

#app.include_router(product_routes.router,prefix="/v1/product", tags=["Products"])
app.include_router(owner_routes.router,prefix="/v1/owner", tags=["Owners"])

app.include_router(pet_routes.router,prefix="/v1/pet", tags=["Pets"])
