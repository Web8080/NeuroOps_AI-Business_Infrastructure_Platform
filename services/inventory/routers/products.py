from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ProductCreate(BaseModel):
    name: str
    sku: str
    quantity: int = 0
    reorder_level: int = 0
    unit: str = "ea"


@router.get("/")
def list_products(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_product(body: ProductCreate):
    raise HTTPException(501, "Not implemented")


@router.get("/{product_id}")
def get_product(product_id: str):
    raise HTTPException(501, "Not implemented")


@router.patch("/{product_id}")
def update_product(product_id: str, body: dict):
    raise HTTPException(501, "Not implemented")
