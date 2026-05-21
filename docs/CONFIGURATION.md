# Configuration Guide

This repository ships OpenClaw skill instructions only. It does **not** include real API keys and does **not** install search providers by itself.

Use these files as safe templates:

- `.env.example` — environment variable placeholders.
- `config/openclaw.skills.example.json` — example `skills.load.extraDirs` fragment.
- `config/openclaw.env.example.json` — generic env placeholder fragment for environments that support config-level env injection.

## 1. API keys

Copy the environment template:

```bash
cp .env.example .env
```

Then edit `.env` locally and fill only the keys your OpenClaw setup actually uses:

```bash
EXA_API_KEY="..."
TAVILY_API_KEY="..."
XAI_API_KEY="..."
```

Do not commit `.env`.

## 2. Installing the skills

Recommended simple install:

```bash
cp -R skills/exa-company-research ~/.openclaw/workspace/skills/
cp -R skills/foreign-trade-research ~/.openclaw/workspace/skills/
openclaw skills list | grep -E 'exa-company-research|foreign-trade-research'
```

Alternative: keep the repository cloned and configure OpenClaw to load this repo's `skills/` directory as an extra skill directory. See `config/openclaw.skills.example.json`.

Before editing OpenClaw's real config, check the current OpenClaw documentation for your version.

## 3. Tool availability

These skills are most useful when your OpenClaw environment exposes these tools:

- `exa_search`
- `dual_search`
- `tavily_search`
- `grok_search`
- `ws_fetch`
- `web_fetch`
- `browser`
- `sessions_spawn`
- `write`
- `update_plan`

If a tool is unavailable, the agent should fall back to available search/fetch tools, but quality may vary.

## 4. Social search safety

The skills only instruct public-source lookup:

- LinkedIn public profiles/pages via `exa_search category="linkedin profile"` and normal web queries.
- X/Twitter public posts via `exa_search category="tweet"`, `grok_search platform="Twitter"`, or domain-limited web search.
- Facebook public pages/posts via `site:facebook.com` searches and browser verification.

They do not authorize logging in, scraping private content, bypassing access controls, or sending messages.

## 5. Key safety checklist before publishing

Run:

```bash
python3 scripts/validate_skills.py
python3 scripts/check_no_secrets.py
```

The secret check is heuristic. Always review the final git diff before publishing.
