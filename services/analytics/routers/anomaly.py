from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class AnomalyRequest(BaseModel):
    metric_name: str
    start_date: str
    end_date: str


@router.post("/detect")
def detect_anomalies(body: AnomalyRequest):
    # TODO: XGBoost or similar on time-series; return anomalies list
    raise HTTPException(501, "Not implemented: XGBoost model placeholder")


@router.get("/alerts")
def list_anomaly_alerts(skip: int = 0, limit: int = 20):
    raise HTTPException(501, "Not implemented")
