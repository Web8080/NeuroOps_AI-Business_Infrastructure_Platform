#!/usr/bin/env bash
# Run DB migrations. Set DATABASE_URL or run inside Docker network.

set -e
cd "$(dirname "$0")/../.."

# TODO: per-service migrations (Alembic or Django)
# Example: alembic -c services/auth/alembic.ini upgrade head
echo "Migration script placeholder. Add Alembic or Django migrate per service."
