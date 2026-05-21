# OpenClaw Exa Research Skills

适用于 OpenClaw 的企业研究与外贸市场调研 skills。

本项目由两个 OpenClaw workspace skills 组成：

- `exa-company-research`：公司研究、竞品分析、企业情报、公开 LinkedIn/X/Facebook 线索补充。
- `foreign-trade-research`：目标国家 + 产品领域的外贸市场调研、竞争格局、经销商/进口商开发、进入策略建议。

> 本项目是 OpenClaw skill 项目，不是 Claude Code `.claude/skills` 项目。已将 Claude Code 的 `Task`、`mcp__exa__...`、`triggers/requires_mcp/context` 等专有约定改写为 OpenClaw 工具和工作流。

## 功能概览

### exa-company-research

适合：

- 公司背景研究
- 竞争对手分析
- 企业情报收集
- 新闻/融资/市场动态追踪
- 公开 LinkedIn 联系人线索
- X/Twitter 公开动态搜索（不依赖已废弃的 Exa tweet category）
- Facebook 公开页面核验

### foreign-trade-research

适合：

- 外贸市场调研
- 海外目标国市场分析
- 品牌商 / 制造商 / 经销商格局识别
- 竞品拆解
- 价格与渠道分析
- 中国供应商进入策略建议
- 经销商/进口商/客户开发名单整理

## 目录结构

```text
openclaw-exa-research-skills/
  README.md
  LICENSE
  .gitignore
  .env.example
  config/
    openclaw.env.example.json
    openclaw.skills.example.json
  docs/
    CONFIGURATION.md
  scripts/
    validate_skills.py
    check_no_secrets.py
  skills/
    exa-company-research/
      SKILL.md
    foreign-trade-research/
      SKILL.md
```

## 安装方式

### 方式一：安装到当前 OpenClaw workspace

```bash
git clone https://github.com/<your-name>/openclaw-exa-research-skills.git
cd openclaw-exa-research-skills
cp -R skills/exa-company-research ~/.openclaw/workspace/skills/
cp -R skills/foreign-trade-research ~/.openclaw/workspace/skills/
openclaw skills list | grep -E 'exa-company-research|foreign-trade-research'
```

### 方式二：安装到全局 skills 目录

```bash
git clone https://github.com/<your-name>/openclaw-exa-research-skills.git
cd openclaw-exa-research-skills
mkdir -p ~/.openclaw/skills
cp -R skills/exa-company-research ~/.openclaw/skills/
cp -R skills/foreign-trade-research ~/.openclaw/skills/
openclaw skills list | grep -E 'exa-company-research|foreign-trade-research'
```

如果当前会话没有立即加载，可新开会话或重启 gateway：

```bash
openclaw gateway restart
```

## 配置文件与 API Key 模板

本仓库提供安全的占位符模板，方便别人 clone 后按自己的环境配置：

- `.env.example`：API Key / 代理环境变量模板，只包含占位符，不包含明文 key。
- `config/openclaw.skills.example.json`：示例 `skills.load.extraDirs` 配置片段。
- `config/openclaw.env.example.json`：示例环境变量配置片段。
- `docs/CONFIGURATION.md`：详细配置说明和安全注意事项。

本仓库不会、也不应该提交真实 `.env` 或真实 API Key。`.gitignore` 已阻止 `.env`、`.env.*`、`*.pem`、`*.key` 等敏感文件提交。

本地配置示例：

```bash
cp .env.example .env
# 编辑 .env，填入自己的真实 API Key；不要提交 .env
```

发布前建议执行：

```bash
python3 scripts/check_no_secrets.py
```

## 依赖工具

这些 skill 本身不包含真实 API Key，也不直接实现搜索 API。它们是 OpenClaw 的工作流说明，依赖 OpenClaw 环境中可用的搜索/浏览工具。

建议环境具备以下工具中的若干项：

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

其中：

- Exa 公司/LinkedIn 类检索依赖 `exa_search`。
- X/Twitter 实时讨论优先用 `grok_search platform="Twitter"`，或用 `site:x.com` / `site:twitter.com` 的普通网页搜索补强；不要再使用已废弃的 Exa `tweet` category。
- Facebook 没有专用 Exa category，使用 `site:facebook.com` + 普通网页搜索/浏览器公开页面验证。

## 使用示例

```text
研究一下 Parker Hannifin 在印度液压软管市场的竞争对手。
```

```text
深度调研印度液压软管市场，输出竞争格局、主要经销商和中国供应商进入建议。
```

```text
整理印度液压软管经销商/进口商开发名单，并补充 LinkedIn、X、Facebook 公开线索。
```

```text
调研巴西工程机械液压软管市场，重点找本地品牌商、制造商、经销商和价格区间。
```

## 社交平台搜索边界

本项目只指导使用公开信息：

- LinkedIn：只搜索公开资料，不登录、不绕过限制、不自动加好友或发私信。
- X/Twitter：只搜索公开内容，不自动关注、点赞、评论、转发或私信。
- Facebook：只搜索公开页面和公开帖子，不登录、不绕过访问限制、不自动点赞、评论、关注、私信或加入群组。

如需使用用户账号、导出联系人、发送消息或进行任何外部互动，必须先由使用者明确授权并遵守平台规则。

## 校验

```bash
python3 scripts/validate_skills.py
python3 scripts/check_no_secrets.py
```

校验内容：

- 每个 skill 是否有 `SKILL.md`
- YAML frontmatter 是否可解析
- 是否包含 `name` 和 `description`
- 当前两个 skill 是否包含 LinkedIn / X / Facebook 公开搜索规则
- 是否已经禁用旧的 Exa `tweet` category 指导，并保留 `grok_search platform="Twitter"` 或 `site:x.com` / `site:twitter.com` 替代口径
- 配置模板是否没有明显明文密钥风险

## 发布到 GitHub

```bash
cd openclaw-exa-research-skills
git init
git add .
git commit -m "Initial OpenClaw Exa research skills"
git branch -M main
git remote add origin https://github.com/<your-name>/openclaw-exa-research-skills.git
git push -u origin main
```

## License

MIT
