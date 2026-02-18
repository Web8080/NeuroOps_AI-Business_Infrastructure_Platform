#!/usr/bin/env bash
# Update Python and Node dependencies. Review diffs before committing.

set -e
cd "$(dirname "$0")/../.."

echo "Updating backend deps (pip)..."
for dir in services/auth services/tenant services/crm services/inventory services/accounting services/billing services/analytics services/ai; do
  if [ -f "$dir/requirements.txt" ]; then
    (cd "$dir" && pip install -r requirements.txt --upgrade 2>/dev/null || true)
  fi
done

echo "Updating frontend deps..."
if [ -d frontend ]; then
  (cd frontend && npm update)
fi
echo "Done. Run tests after updating."
