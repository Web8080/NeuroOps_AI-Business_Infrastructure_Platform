from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ForecastRequest(BaseModel):
    series_id: str
    horizon_days: int = 30


@router.post("/demand")
def demand_forecast(body: ForecastRequest):
    # TODO: Prophet (or similar) on series; return forecast points
    raise HTTPException(501, "Not implemented: Prophet placeholder")
