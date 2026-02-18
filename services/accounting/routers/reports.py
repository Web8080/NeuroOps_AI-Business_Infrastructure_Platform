from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/pl")
def profit_loss():
    raise HTTPException(501, "Not implemented")


@router.get("/balance-sheet")
def balance_sheet():
    raise HTTPException(501, "Not implemented")
