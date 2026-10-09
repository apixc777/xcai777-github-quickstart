"""Minimal XCAI777 Responses API example using only the Python standard library."""

import json
import os
from urllib.request import Request, urlopen


def main() -> None:
    api_key = os.environ.get("XCAI777_API_KEY")
    model = os.environ.get("XCAI777_MODEL")
    if not api_key or not model:
        raise SystemExit(
            "请先设置 XCAI777_API_KEY 和 XCAI777_MODEL 环境变量。"
        )

    base_url = os.environ.get("XCAI777_BASE_URL", "https://7777777api.com/v1").rstrip("/")
    request = Request(
        f"{base_url}/responses",
        data=json.dumps(
            {
                "model": model,
                "input": "请用三句话介绍一个适合新手的 AI 自动化应用点子。",
            }
        ).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urlopen(request, timeout=120) as response:
        payload = json.load(response)

    # Responses API usually returns output_text; also handle a structured output
    # array for gateways that omit the convenience field.
    if payload.get("output_text"):
        print(payload["output_text"])
        return

    texts = [
        content.get("text", "")
        for item in payload.get("output", [])
        for content in item.get("content", [])
        if content.get("type") == "output_text"
    ]
    if texts:
        print("\n".join(texts))
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
