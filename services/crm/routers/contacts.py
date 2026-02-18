from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()


class ContactCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None


@router.get("/")
def list_contacts(skip: int = 0, limit: int = 20):
    # TODO: tenant from JWT; RLS; RBAC crm:read
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_contact(body: ContactCreate):
    # TODO: tenant; RBAC crm:write; audit
    raise HTTPException(501, "Not implemented")


@router.get("/{contact_id}")
def get_contact(contact_id: str):
    raise HTTPException(501, "Not implemented")


@router.patch("/{contact_id}")
def update_contact(contact_id: str, body: dict):
    raise HTTPException(501, "Not implemented")


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: str):
    raise HTTPException(501, "Not implemented")
