#!/usr/bin/env bash
# Placeholder: simulate tenant load for performance testing.
# Requires a running stack and tools like ab, hey, or k6.

set -e
BASE="${1:-http://localhost:8000}"
echo "Health check..."
curl -s -o /dev/null -w "%{http_code}" "$BASE/health" || true
echo ""
echo "Load test placeholder. Add: hey -n 1000 -c 10 $BASE/health"
