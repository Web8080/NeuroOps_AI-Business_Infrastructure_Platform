#!/usr/bin/env bash
# Restore ~/.docker/config.json from backup (if you applied the credsStore patch).
set -e
cd "$(dirname "$0")/../.."
BAK=".docker-config.json.bak"
if [ -f "$BAK" ]; then
  cp "$BAK" ~/.docker/config.json
  echo "Restored ~/.docker/config.json from $BAK"
else
  echo "No backup found at $BAK. Restore credsStore manually in ~/.docker/config.json if needed."
fi
