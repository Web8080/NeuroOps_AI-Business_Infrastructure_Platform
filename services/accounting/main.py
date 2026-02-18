"""Accounting service: chart of accounts, journals, invoices, reports."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import accounts, journals, invoices, reports

app = FastAPI(title="NeuroOps Accounting", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(accounts.router, prefix="/api/v1/accounts", tags=["accounts"])
app.include_router(journals.router, prefix="/api/v1/journals", tags=["journals"])
app.include_router(invoices.router, prefix="/api/v1/invoices", tags=["invoices"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])


@app.get("/health")
def health():
    return {"status": "ok"}
