"""Billing service: Stripe sync, webhooks, plan/feature gating."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import subscription, webhooks

app = FastAPI(title="NeuroOps Billing", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(subscription.router, prefix="/api/v1/subscription", tags=["subscription"])
app.include_router(webhooks.router, prefix="/api/v1/webhooks/stripe", tags=["webhooks"])


@app.get("/health")
def health():
    return {"status": "ok"}
