"""Unit tests for auth endpoints. Run without AWS or real DB."""

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_register_returns_501_without_impl():
    r = client.post("/api/v1/auth/register", json={
        "email": "u@example.com",
        "password": "secret",
        "tenant_slug": "acme",
    })
    assert r.status_code == 501


def test_login_returns_501_without_impl():
    r = client.post("/api/v1/auth/login", json={
        "email": "u@example.com",
        "password": "secret",
    })
    assert r.status_code == 501
