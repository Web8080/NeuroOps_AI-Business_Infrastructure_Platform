"""Audit logging interface. Implement backend (DB or Kafka) per service."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID


def log_audit(
    action: str,
    resource_type: str,
    resource_id: Optional[str] = None,
    tenant_id: Optional[UUID] = None,
    user_id: Optional[UUID] = None,
    outcome: str = "success",
    details: Optional[dict[str, Any]] = None,
    ip: Optional[str] = None,
) -> None:
    """Append an audit log entry. Default implementation no-op; replace with DB or Kafka."""
    # TODO: write to audit table or Kafka topic; include timestamp, correlation_id
    _ = action
    _ = resource_type
    _ = resource_id
    _ = tenant_id
    _ = user_id
    _ = outcome
    _ = details
    _ = ip
    _ = datetime.utcnow()
