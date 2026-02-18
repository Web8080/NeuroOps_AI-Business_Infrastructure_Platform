#!/usr/bin/env bash
# Run unit tests for backend services. No AWS or live DB required.

set -e
cd "$(dirname "$0")/../.."

pip install pytest httpx 2>/dev/null || true
echo "Running auth tests..."
pip install -r services/auth/requirements.txt
cd services/auth && python -m pytest tests/ -v && cd ../..
echo "Running tenant tests..."
pip install -r services/tenant/requirements.txt
cd services/tenant && python -m pytest tests/ -v && cd ../..
echo "Backend unit tests done."
