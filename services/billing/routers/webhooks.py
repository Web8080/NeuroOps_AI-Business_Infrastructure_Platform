import os
from fastapi import APIRouter, Request, HTTPException

router = APIRouter()


@router.post("")
async def stripe_webhook(request: Request):
    # TODO: read raw body; verify stripe signature with STRIPE_WEBHOOK_SECRET
    # Handle subscription.created, updated, deleted, invoice.paid, payment_failed
    # Idempotent by event id; update tenant subscription in DB
    secret = os.environ.get("STRIPE_WEBHOOK_SECRET")
    if not secret:
        raise HTTPException(503, "STRIPE_WEBHOOK_SECRET not configured")
    payload = await request.body()
    # sig = request.headers.get("Stripe-Signature")
    # stripe.Webhook.construct_event(payload, sig, secret)
    return {"received": True}
