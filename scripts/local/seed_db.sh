#!/usr/bin/env bash
# Placeholder: seed database with demo tenant and user.
# Requires DATABASE_URL or run from same network as postgres container.

set -e
cd "$(dirname "$0")/../.."

# TODO: run migrations first (Alembic or Django migrate)
# TODO: insert demo tenant, super_admin user, sample CRM/accounting data
echo "Seed script placeholder. Implement migrations and seed data per service."
