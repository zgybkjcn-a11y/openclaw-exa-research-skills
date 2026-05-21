#!/usr/bin/env python3
"""Heuristic secret scanner for this repository.

It allows known placeholders like YOUR_EXA_API_KEY_HERE, but flags common
accidental secret patterns. This is not a substitute for manual review.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
TEXT_EXTS = {".md", ".py", ".json", ".example", ".gitignore", ".txt", ""}
ALLOW_PLACEHOLDERS = [
    "YOUR_EXA_API_KEY_HERE",
    "YOUR_TAVILY_API_KEY_HERE",
    "YOUR_XAI_API_KEY_HERE",
    "YOUR_GROK_API_KEY_HERE",
    "YOUR_OPENAI_API_KEY_HERE",
    "YOUR_ANTHROPIC_API_KEY_HERE",
]
PATTERNS = [
    ("OpenAI key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("Anthropic key", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}")),
    ("Generic API assignment", re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*[\"']?(?!YOUR_|PLACEHOLDER|CHANGE_ME|<)[A-Za-z0-9_\-]{24,}")),
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----")),
]

findings = []
for path in ROOT.rglob("*"):
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.is_dir():
        continue
    if path.name == ".env":
        findings.append((path, "Real .env file should not be committed"))
        continue
    if path.suffix not in TEXT_EXTS and not path.name.endswith(".example"):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    sanitized = text
    for ph in ALLOW_PLACEHOLDERS:
        sanitized = sanitized.replace(ph, "PLACEHOLDER")
    for label, pattern in PATTERNS:
        if pattern.search(sanitized):
            findings.append((path, label))

if findings:
    for path, label in findings:
        print(f"[WARN] {label}: {path.relative_to(ROOT)}")
    sys.exit(1)

print("[OK] no obvious secrets found")
