from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class MovementCreate(BaseModel):
    product_id: str
    quantity_delta: int
    type: str  # in, out, adjust
    reason: str | None = None


@router.get("/")
def list_movements(product_id: str | None = None, skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_movement(body: MovementCreate):
    raise HTTPException(501, "Not implemented")
