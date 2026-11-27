#!/usr/bin/env python3
"""Build the deterministic canon index (`_index.json`).

Deterministic by construction: entries are sorted by path and the file contains no
timestamps, so a second run produces an identical byte stream. Run from anywhere:

    python3 bin/build_index.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_TOP = {"bin", ".git", "_site"}
FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
INLINE_LIST = re.compile(r"^\[(.*)\]$")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _tags(value: str) -> list[str]:
    inline = INLINE_LIST.match(value.strip())
    if inline:
        return [_unquote(item) for item in inline.group(1).split(",") if item.strip()]
    return []


def front_matter(text: str) -> dict[str, object]:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    meta: dict[str, object] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        if key == "tags":
            meta["tags"] = _tags(value)
        elif key in {"uid", "title"}:
            meta[key] = _unquote(value)
    return meta


def build() -> dict[str, object]:
    documents = []
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if relative.parts[0] in SKIP_TOP:
            continue
        meta = front_matter(path.read_text(encoding="utf-8", errors="replace"))
        documents.append(
            {
                "path": relative.as_posix(),
                "uid": str(meta.get("uid", "")),
                "title": str(meta.get("title", "")),
                "tags": list(meta.get("tags", [])),
            }
        )
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    return {
        "schema_version": 1,
        "canon_version": version,
        "total_entries": len(documents),
        "documents": documents,
    }


def main() -> int:
    payload = build()
    target = ROOT / "_index.json"
    target.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {target.relative_to(ROOT)} with {payload['total_entries']} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
