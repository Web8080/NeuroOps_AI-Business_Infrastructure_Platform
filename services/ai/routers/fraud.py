from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class FraudScoreRequest(BaseModel):
    transaction_id: str
    amount_cents: int
    customer_id: str
    payload: dict | None = None


@router.post("/score")
def score_fraud(body: FraudScoreRequest):
    # TODO: XGBoost or rule-based score; return score 0-1 and alert threshold
    raise HTTPException(501, "Not implemented: fraud model placeholder")


@router.get("/alerts")
def list_fraud_alerts(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")
