"""Tenant context for request-scoped isolation. Set by auth middleware from JWT or header."""

from __future__ import annotations

from typing import Optional
from uuid import UUID


def get_tenant_id() -> Optional[UUID]:
    """Return current request tenant_id from context (e.g. contextvars). Placeholder."""
    # TODO: implement via contextvars set in auth middleware
    return None


def get_current_user_id() -> Optional[UUID]:
    """Return current user id from context. Placeholder."""
    return None


def get_current_roles() -> list[str]:
    """Return current user roles for this tenant. Placeholder."""
    return []
