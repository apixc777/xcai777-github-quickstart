#!/usr/bin/env bash
set -euo pipefail

: "${XCAI777_API_KEY:?请先设置 XCAI777_API_KEY}"
: "${XCAI777_MODEL:?请先设置 XCAI777_MODEL}"

curl --fail-with-body --silent --show-error \
  -X POST "${XCAI777_BASE_URL:-https://7777777api.com/v1}/responses" \
  -H "Authorization: Bearer ${XCAI777_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(python - <<'PY'
import json
import os

print(json.dumps({
    "model": os.environ["XCAI777_MODEL"],
    "input": "请用三句话介绍一个适合新手的 AI 自动化应用点子。",
}))
PY
)"

