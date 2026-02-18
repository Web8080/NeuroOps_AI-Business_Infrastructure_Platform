"""RBAC helpers: permission checks and role definitions."""

from __future__ import annotations

from enum import Enum
from typing import Set

from .tenant import get_current_roles


class Role(str, Enum):
    SUPER_ADMIN = "super_admin"
    TENANT_ADMIN = "tenant_admin"
    END_USER = "end_user"


# Permissions per role (add more as needed)
ROLE_PERMISSIONS: dict[Role, Set[str]] = {
    Role.SUPER_ADMIN: {"*"},
    Role.TENANT_ADMIN: {
        "tenant:read", "tenant:write", "users:read", "users:write",
        "crm:*", "inventory:*", "accounting:*", "analytics:*", "billing:*", "ai:*",
    },
    Role.END_USER: {
        "crm:read", "crm:write", "inventory:read", "inventory:write",
        "accounting:read", "analytics:read", "ai:chat",
    },
}


def has_permission(required: str) -> bool:
    """Check if current user has required permission (e.g. 'crm:write'). Wildcard * means all."""
    roles = get_current_roles()
    for r in roles:
        try:
            role = Role(r)
        except ValueError:
            continue
        perms = ROLE_PERMISSIONS.get(role, set())
        if "*" in perms:
            return True
        if required in perms:
            return True
        # prefix match e.g. crm:* for crm:read
        if ":" in required:
            prefix = required.split(":")[0] + ":*"
            if prefix in perms:
                return True
    return False


def require_permission(required: str) -> None:
    """Raise 403 if current user lacks permission."""
    if not has_permission(required):
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Insufficient permissions")
