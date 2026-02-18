from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class CheckoutBody(BaseModel):
    price_id: str
    success_url: str
    cancel_url: str
    trial_days: int = 7


@router.get("/")
def get_subscription():
    # TODO: tenant from JWT; return current plan, trial end, status
    raise HTTPException(501, "Not implemented")


@router.post("/checkout")
def create_checkout_session(body: CheckoutBody):
    # TODO: Stripe Checkout Session; return session.url
    raise HTTPException(501, "Not implemented: set STRIPE_SECRET_KEY")


@router.post("/portal")
def customer_portal(return_url: str):
    # TODO: Stripe Customer Portal session
    raise HTTPException(501, "Not implemented")
