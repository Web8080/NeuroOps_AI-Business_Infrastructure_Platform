from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class InvoiceCreate(BaseModel):
    contact_id: str
    amount_cents: int
    due_date: str
    line_items: list[dict] = []


@router.get("/")
def list_invoices(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_invoice(body: InvoiceCreate):
    raise HTTPException(501, "Not implemented")


@router.get("/{invoice_id}")
def get_invoice(invoice_id: str):
    raise HTTPException(501, "Not implemented")
