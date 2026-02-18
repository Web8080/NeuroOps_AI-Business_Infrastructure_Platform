"""CRM service: contacts, deals, activities."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import contacts, deals

app = FastAPI(title="NeuroOps CRM", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(contacts.router, prefix="/api/v1/contacts", tags=["contacts"])
app.include_router(deals.router, prefix="/api/v1/deals", tags=["deals"])


@app.get("/health")
def health():
    return {"status": "ok"}
