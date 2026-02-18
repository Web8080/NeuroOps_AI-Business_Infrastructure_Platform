"""Analytics service: dashboards, anomaly detection, demand forecasting."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import dashboards, anomaly, forecasting

app = FastAPI(title="NeuroOps Analytics", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(dashboards.router, prefix="/api/v1/dashboards", tags=["dashboards"])
app.include_router(anomaly.router, prefix="/api/v1/anomaly", tags=["anomaly"])
app.include_router(forecasting.router, prefix="/api/v1/forecasting", tags=["forecasting"])


@app.get("/health")
def health():
    return {"status": "ok"}
