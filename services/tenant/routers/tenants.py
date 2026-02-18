from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class TenantCreate(BaseModel):
    name: str
    slug: str


@router.get("/")
def list_tenants():
    # TODO: Super Admin only; RLS or service-level tenant filter
    raise HTTPException(501, "Not implemented")


@router.post("/", status_code=201)
def create_tenant(body: TenantCreate):
    # TODO: Super Admin only; create tenant and default settings
    raise HTTPException(501, "Not implemented")


@router.get("/{tenant_id}")
def get_tenant(tenant_id: str):
    # TODO: resolve tenant; check permission tenant:read
    raise HTTPException(501, "Not implemented")


@router.patch("/{tenant_id}")
def update_tenant(tenant_id: str, body: dict):
    # TODO: Tenant Admin or Super Admin; audit log
    raise HTTPException(501, "Not implemented")
