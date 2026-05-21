---
name: exa-company-research
description: "使用 OpenClaw 的 Exa/联网搜索工具进行公司研究、竞品分析、企业情报、新闻动态、融资信息和公开 LinkedIn 资料检索。"
allowed-tools: ["exa_search", "tavily_search", "grok_search", "ws_fetch", "web_fetch", "browser", "sessions_spawn", "write", "update_plan"]
---

# Exa Company Research

用于以下任务：

- 公司研究
- 企业情报收集
- 竞争对手分析
- 市场参与者列表构建
- 公司新闻、融资、财务、社交媒体、公开 LinkedIn 资料整理

## OpenClaw 工具映射

优先使用 `exa_search`。

可补充使用：

- `tavily_search`：常规网页结果补强
- `grok_search`：复杂问题综合分析、实时信息补强
- `ws_fetch` / `web_fetch`：抓取具体网页正文
- `browser`：搜索结果不足、页面需要 JS 渲染、需要人工可视化验证时使用
- `sessions_spawn`：大型调研时派发子任务，避免主上下文污染
- `write`：用户要求保存报告时写入 markdown 文件

## 重要原则

### 1. 不在主上下文堆大量搜索结果

如果用户要求“深度研究 / 全面调研 / 找 50 家以上 / 输出完整报告”，优先使用 `sessions_spawn` 拆分子任务。

子任务只返回：

- 去重后的候选公司列表
- 关键事实
- 来源链接
- 置信度
- 未确认点

不要让子任务返回大段原始搜索结果。

### 2. 动态调整搜索深度

根据用户意图调整 `exa_search.numResults`：

- 快速了解：10-20
- 标准研究：20-40
- 深度研究：50-100
- 用户指定数量：按用户要求执行

不确定时，只问一个问题：

> 您需要快速了解、标准研究，还是深度研究？

### 3. 查询变体

每个研究主题生成 2-3 个查询变体。

例如研究某公司竞争对手：

- `[company] competitors market share 2025`
- `[company] alternatives similar companies industry`
- `[industry] leading companies competitors [country]`

合并结果后去重。

### 4. Exa category 使用规则

OpenClaw `exa_search` 的 `category` 只用于仍受支持的定向检索：

- `company`：公司主页、公司基础信息
- `news`：新闻报道、融资、并购、市场动态
- `linkedin profile`：公开 LinkedIn 人员资料
- X/Twitter 公开动态：不要再使用已废弃的 tweet 分类；优先用 `grok_search` with `platform: "Twitter"`，或用 `site:x.com` / `site:twitter.com` 的普通网页搜索补强
- 不确定时可不指定 category，作为普通语义搜索，或分多次搜索

### 5. 输出结构

公司研究默认输出：

```markdown
## 一、结论摘要

## 二、公司基本信息
- 公司名称：
- 官网：
- 总部：
- 成立时间：
- 主营业务：
- 员工规模：
- 融资/财务情况：
- 主要市场：

## 三、主要竞争对手

## 四、近期动态

## 五、风险与不确定信息

## 六、来源链接
```

### 6. 浏览器回退

以下情况使用 `browser`：

- Exa 结果不足
- 页面需要 JavaScript 渲染
- 需要验证官网、产品页、价格页
- 需要查看动态网页内容

使用浏览器前，如果涉及登录、付费、隐私或外部动作，先询问用户。

### 7. LinkedIn 公开线索搜索

当任务涉及客户开发、经销商开发、联系人查找、关键人员识别时，使用 `exa_search` 的 `linkedin profile` category 检索公开 LinkedIn 资料。

优先搜索角色：

- Owner / Founder / Co-founder / Managing Director / Director
- Sales Manager / Business Development Manager / Regional Sales Manager
- Purchase Manager / Procurement Manager / Sourcing Manager
- Export Manager / Import Manager / International Business Manager
- Industry-specific roles, e.g. Hydraulic / Fluid Power / Hose / Industrial Supply / MRO

查询示例：

```text
"[Company Name]" "LinkedIn" "Sales Manager"
"[Company Name]" "hydraulic hose" "LinkedIn"
"India hydraulic hose distributor owner LinkedIn"
"Parker hose distributor India sales manager LinkedIn"
"[Industry]" "[Country]" "business development manager" "LinkedIn"
```

执行要求：

- 只使用公开资料；不登录、不绕过 LinkedIn 访问限制。
- 不自动加好友、不自动发私信、不批量抓取非公开信息。
- 如果需要登录后的内容、导出联系人、发送消息或其他外部账号操作，先向用户确认。
- 输出客户/公司开发名单时，可增加这些字段：`LinkedIn线索`、`可能联系人`、`职位`、`公开链接`、`置信度`、`备注`。

### 8. X / Twitter 公开信息搜索

当任务涉及市场热度、客户声音、行业讨论、品牌口碑、展会活动、招聘动态、经销商动态、采购线索或实时事件时，使用 X/Twitter 公开信息作为补充信源。

优先工具：

- `grok_search` with `platform: "Twitter"`：优先用于补充实时讨论、趋势和平台内语义搜索（如当前环境支持）。
- `tavily_search` / `dual_search` / `web_search`：搜索 `site:x.com` 或 `site:twitter.com` 公开页面。
- `exa_search`：不要再使用已废弃的 tweet 分类；可不指定 category，作为普通语义搜索补充。
- `browser`：必要时打开公开 X/Twitter 页面做可视化验证；如页面要求登录或出现访问限制，不绕过。

适合搜索的内容：

- 公司或品牌官方账号动态
- 展会参展、代理商活动、产品发布
- 客户投诉、使用反馈、召回或质量争议
- 行业关键词讨论和热门话题
- 经销商、销售人员、采购人员公开发布的信息
- 招聘信息中透露的市场扩张、渠道建设、区域布局

查询示例：

```text
"[Company Name]" "hydraulic hose" site:x.com
"[Brand]" "India" "distributor" "hydraulic hose" Twitter
"[Product]" "[Country]" "dealer" "X"
"[Industry]" "exhibition" "India" "hydraulic" site:twitter.com
"[Company Name]" "hiring" "sales" "India" site:x.com
```

输出要求：

- 明确标注 X/Twitter 信息属于公开社交信号，通常只能作为线索或佐证，不单独作为事实结论。
- 对负面评价、投诉、传言类内容要交叉验证，不要直接定性。
- 输出客户开发名单时，可增加字段：`X线索`、`账号/帖子链接`、`线索类型`、`时间`、`置信度`、`需验证事项`。

边界要求：

- 只检索公开内容；不登录、不绕过访问限制。
- 不自动关注、点赞、评论、转发、私信。
- 如需使用用户账号、发送消息或进行任何外部互动，必须先向用户确认。

### 9. Facebook 公开信息搜索

当任务涉及海外客户开发、经销商核验、门店/仓库/展会活动、区域代理动态、产品促销、WhatsApp/电话线索或本地市场活跃度判断时，使用公开 Facebook 页面作为补充信源。

Facebook 没有专用 `exa_search` category，优先通过域名限定和普通网页搜索完成：

- `tavily_search` / `dual_search` / `web_search`：搜索 `site:facebook.com` 公开页面。
- `exa_search`：不指定 category，使用普通语义搜索补充。
- `browser`：打开公开 Facebook 页面做可视化验证；如页面要求登录或出现访问限制，不绕过。

适合搜索的内容：

- 公司 Facebook Page、门店页面、经销商页面
- 公司动态、产品照片、展会照片、促销活动
- WhatsApp、电话、邮箱、地址、营业时间
- 客户评论、公开留言、投诉或售后反馈
- 区域代理、零售门店、仓库和服务车等本地化线索
- 招聘或扩张信息中透露的销售区域和渠道建设

查询示例：

```text
site:facebook.com "[Company Name]" "[Product]"
site:facebook.com "[Brand]" "[Country]" "distributor"
site:facebook.com "[Product]" "[Country]" "dealer"
"[Company Name]" "Facebook page"
"[Industry]" "[Country]" "dealer" "Facebook"
"[Company Name]" "WhatsApp" "Facebook"
```

输出要求：

- 明确标注 Facebook 信息属于公开社交线索或佐证，不单独作为正式事实结论。
- 对评论、投诉、传言、促销宣传等内容要交叉验证，不要直接定性。
- 输出客户/公司开发名单时，可增加字段：`Facebook线索`、`Facebook主页/帖子链接`、`线索类型`、`最近活跃时间`、`联系方式`、`WhatsApp/电话`、`置信度`、`需验证事项`。

边界要求：

- 只检索公开页面和公开帖子；不登录、不绕过访问限制。
- 不自动点赞、评论、关注、私信、加入群组。
- 如需使用用户账号、发送消息或进行任何外部互动，必须先向用户确认。
