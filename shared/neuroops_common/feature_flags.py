"""Feature flags and canary placeholders. Resolve from DB or config per tenant."""

from __future__ import annotations

from typing import Optional


def is_enabled(flag: str, tenant_id: Optional[str] = None) -> bool:
    """Return True if feature flag is enabled for tenant (or globally). Placeholder."""
    # TODO: load from DB or env; tenant override
    _ = tenant_id
    _ = flag
    return True


def canary_percentage(service: str, tenant_id: Optional[str] = None) -> int:
    """Return 0-100 percentage of traffic to send to canary. Placeholder."""
    # TODO: config per service/tenant
    _ = service
    _ = tenant_id
    return 0
