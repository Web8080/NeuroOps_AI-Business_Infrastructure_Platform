#!/usr/bin/env bash
# Run full stack locally: Docker Compose for backend + optional frontend dev server.
# From repo root: ./scripts/local/run_all.sh

set -e
cd "$(dirname "$0")/../.."

echo "Building and starting backend services..."
docker compose build
docker compose up -d postgres redis
echo "Waiting for Postgres and Redis..."
sleep 5
docker compose up -d
echo "Backend should be up. Auth: http://localhost:8000/health, Tenant: 8001, CRM: 8002, etc."
echo "To run frontend: cd frontend && npm install && npm run dev"
echo "To run E2E: cd frontend && npm run test:e2e"
