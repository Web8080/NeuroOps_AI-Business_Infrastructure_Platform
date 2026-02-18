from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class LineItem(BaseModel):
    account_id: str
    debit_cents: int = 0
    credit_cents: int = 0


class JournalCreate(BaseModel):
    date: str
    description: str
    lines: list[LineItem]


@router.get("/")
def list_journals(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_journal(body: JournalCreate):
    raise HTTPException(501, "Not implemented")
