"""Auth endpoints: register, login, refresh, password reset."""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()


class RegisterBody(BaseModel):
    email: EmailStr
    password: str
    tenant_slug: str | None = None
    invite_token: str | None = None


class LoginBody(BaseModel):
    email: EmailStr
    password: str
    tenant_id: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


@router.post("/register", response_model=TokenResponse)
def register(body: RegisterBody):
    # TODO: validate tenant_slug or invite_token; create user; hash password; create JWT
    # Placeholder: return mock tokens for local testing
    raise HTTPException(501, "Not implemented: set JWT_SECRET_KEY and implement user creation")


@router.post("/login", response_model=TokenResponse)
def login(body: LoginBody):
    # TODO: verify credentials; load tenant membership; issue JWT with tenant_id and roles
    raise HTTPException(501, "Not implemented: implement credential check and JWT issue")


@router.post("/refresh", response_model=TokenResponse)
def refresh(refresh_token: str):
    # TODO: validate refresh token; issue new access + refresh
    raise HTTPException(501, "Not implemented")


@router.post("/forgot-password")
def forgot_password(email: EmailStr):
    # TODO: create reset token; send email (placeholder)
    return {"message": "If the email exists, a reset link was sent"}


@router.post("/reset-password")
def reset_password(token: str, new_password: str):
    # TODO: validate token; update password; invalidate token
    raise HTTPException(501, "Not implemented")
