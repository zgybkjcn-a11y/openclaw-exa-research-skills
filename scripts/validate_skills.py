#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "exa-company-research": [
        "linkedin profile",
        "site:x.com",
        "TweetClaw",
        "Facebook 公开信息搜索",
        "不要再使用已废弃的 tweet 分类",
    ],
    "foreign-trade-research": [
        "linkedin profile",
        "site:x.com",
        "TweetClaw",
        "Facebook 公开信息搜索",
        "不要再使用已废弃的 tweet 分类",
    ],
}

FORBIDDEN_SKILL_PHRASES = [
    "`tweet`：",
    "category=\"tweet\"",
    "category='tweet'",
    "tweet category 使用规则",
    "tweet 分类使用规则",
]

OPTIONAL_FILES = [ROOT / ".env.example", ROOT / "config" / "openclaw.skills.example.json", ROOT / "config" / "openclaw.env.example.json", ROOT / "docs" / "CONFIGURATION.md"]

errors = []

for required in OPTIONAL_FILES:
    if not required.exists():
        errors.append(f"missing helper/config file: {required.relative_to(ROOT)}")

if not SKILLS.exists():
    errors.append(f"missing skills directory: {SKILLS}")
else:
    for name, required_phrases in EXPECTED.items():
        skill_dir = SKILLS / name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"missing {skill_md}")
            continue
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"missing YAML frontmatter: {skill_md}")
            continue
        try:
            fm = text.split("---", 2)[1]
            data = yaml.safe_load(fm)
        except Exception as exc:
            errors.append(f"invalid YAML frontmatter in {skill_md}: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"frontmatter is not a mapping: {skill_md}")
            continue
        if data.get("name") != name:
            errors.append(f"name mismatch in {skill_md}: expected {name!r}, got {data.get('name')!r}")
        if not data.get("description"):
            errors.append(f"missing description in {skill_md}")
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"missing phrase {phrase!r} in {skill_md}")
        for phrase in FORBIDDEN_SKILL_PHRASES:
            if phrase in text:
                errors.append(
                    f"deprecated Exa tweet category guidance remains in {skill_md}: {phrase!r}"
                )

for json_file in [ROOT / "config" / "openclaw.skills.example.json", ROOT / "config" / "openclaw.env.example.json"]:
    if json_file.exists():
        try:
            import json
            json.loads(json_file.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON in {json_file.relative_to(ROOT)}: {exc}")

if errors:
    for err in errors:
        print(f"[ERROR] {err}")
    sys.exit(1)

print("[OK] skills validated")
