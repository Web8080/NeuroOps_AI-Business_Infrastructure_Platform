from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class DealCreate(BaseModel):
    name: str
    contact_id: str | None = None
    value_cents: int = 0
    stage: str = "lead"


@router.get("/")
def list_deals(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_deal(body: DealCreate):
    raise HTTPException(501, "Not implemented")


@router.get("/{deal_id}")
def get_deal(deal_id: str):
    raise HTTPException(501, "Not implemented")
