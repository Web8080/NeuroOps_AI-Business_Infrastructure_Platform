from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class AccountCreate(BaseModel):
    code: str
    name: str
    type: str  # income, expense, asset, liability, equity


@router.get("/")
def list_accounts():
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_account(body: AccountCreate):
    raise HTTPException(501, "Not implemented")
