"""Inventory service: products, stock, movements."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import products, movements

app = FastAPI(title="NeuroOps Inventory", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(movements.router, prefix="/api/v1/movements", tags=["movements"])


@app.get("/health")
def health():
    return {"status": "ok"}
