"""Tenant service: tenant CRUD, org settings, user-tenant-role mapping."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import tenants

app = FastAPI(title="NeuroOps Tenant", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(tenants.router, prefix="/api/v1/tenants", tags=["tenants"])


@app.get("/health")
def health():
    return {"status": "ok"}
