#!/usr/bin/env bash
# Placeholder: send alert to Slack. Set SLACK_WEBHOOK_URL in env (ask user for URL).

SLACK_WEBHOOK_URL="${SLACK_WEBHOOK_URL:-}"
TEXT="${1:-NeuroOps alert}"

if [ -z "$SLACK_WEBHOOK_URL" ]; then
  echo "SLACK_WEBHOOK_URL not set. Skipping Slack notification."
  exit 0
fi
curl -s -X POST -H 'Content-type: application/json' \
  --data "{\"text\":\"$TEXT\"}" \
  "$SLACK_WEBHOOK_URL" || true
