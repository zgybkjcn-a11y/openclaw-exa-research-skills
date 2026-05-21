---
name: foreign-trade-research
description: "针对目标国家和产品领域进行外贸市场调研、竞争格局识别、竞品拆解、渠道分析、价格分析和中国供应商进入策略建议。"
allowed-tools: ["exa_search", "dual_search", "tavily_search", "grok_search", "ws_fetch", "web_fetch", "browser", "sessions_spawn", "write", "update_plan"]
---

# Foreign Trade Research

用于以下任务：

- 外贸市场调研
- 海外市场分析
- 目标国市场调研
- 竞争对手分析
- 中国供应商出海策略
- 品牌商 / 制造商 / 经销商格局分析

## 总原则

这是深度调研型 skill。用户明确说：

- 外贸市场调研
- 深度调研
- 系统研究
- 目标国市场分析
- 竞争对手分析
- 海外市场进入策略

应使用本 skill。

如任务较大，必须使用 `sessions_spawn` 拆分子任务，避免主上下文堆积搜索结果。

## 推荐工具链

优先顺序：

1. `exa_search`：公司、新闻、社交、LinkedIn 等定向搜索
2. `dual_search`：需要覆盖多个搜索视角时使用
3. `tavily_search`：常规网页补强
4. `grok_search`：复杂问题综合分析和实时信息补强
5. `ws_fetch` / `web_fetch`：抓取重点网页正文
6. `browser`：动态网页、电商页面、需要可视化确认时使用

## 调研流程

### 第一步：识别竞争格局

目标：找出目标国家 + 产品领域的 TOP 活跃公司。

默认分三类：

- 本土品牌商：TOP 7
- 制造商：TOP 7
- 经销商 / 批发商 / 进口商：TOP 6

每家公司至少包含：

- 公司全称
- 国家 / 城市
- 官方网站
- 公司类型
- 主要产品
- 市场地位
- 来源链接
- 置信度

搜索查询示例：

```text
[Country] [Product] leading brands manufacturers distributors 2025
top [Product] companies in [Country] market share
[Country] [Product] importers wholesalers suppliers
```

如果目标国非英语国家，增加当地语言关键词。

### 第二步：逐个拆解竞品

对重点公司分析：

- 公司背景
- 产品线
- 定价策略
- 主要客户
- 销售渠道
- 优势
- 劣势
- 对中国供应商的威胁或机会

搜索查询示例：

```text
[Company Name] [Product] company profile revenue employees
[Company Name] [Product] pricing distributors customers
[Company Name] reviews complaints competitors
```

### 第三步：生成竞争对比矩阵

矩阵字段：

- 公司名称
- 类型
- 市场地位
- 核心产品
- 价格定位
- 渠道
- 主要客户
- 优势
- 劣势
- 对中国供应商启示

### 第四步：多源验证

重点验证：

- 官网产品信息
- 电商 / B2B 平台价格
- 新闻报道
- 社交媒体
- LinkedIn 公开信息
- 客户评价

如 Exa 结果不足，使用 `browser` 或 `ws_fetch` 补充。

#### LinkedIn 公开线索搜索

当外贸市场调研进入客户开发、经销商开发、联系人查找、关键人员识别阶段时，使用 `exa_search` 的 `linkedin profile` category 检索公开 LinkedIn 资料。

优先搜索角色：

- Owner / Founder / Co-founder / Managing Director / Director
- Sales Manager / Business Development Manager / Regional Sales Manager
- Purchase Manager / Procurement Manager / Sourcing Manager
- Export Manager / Import Manager / International Business Manager
- Hydraulic / Fluid Power / Hose / Industrial Supply / MRO 等行业相关岗位

查询示例：

```text
"[Company Name]" "LinkedIn" "Sales Manager"
"[Company Name]" "hydraulic hose" "LinkedIn"
"India hydraulic hose distributor owner LinkedIn"
"Parker hose distributor India sales manager LinkedIn"
"[Product]" "[Country]" "import manager" "LinkedIn"
"[Industry]" "[Country]" "business development manager" "LinkedIn"
```

执行要求：

- 只使用公开资料；不登录、不绕过 LinkedIn 访问限制。
- 不自动加好友、不自动发私信、不批量抓取非公开信息。
- 如果需要登录后的内容、导出联系人、发送消息或其他外部账号操作，先向用户确认。
- 输出经销商/进口商/客户开发名单时，建议增加字段：`LinkedIn线索`、`可能联系人`、`职位`、`公开链接`、`置信度`、`备注`。

#### X / Twitter 公开信息搜索

当外贸市场调研进入市场热度、客户声音、品牌口碑、展会活动、经销商动态、采购线索、招聘扩张或实时事件验证阶段时，使用 X/Twitter 公开信息作为补充信源。

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
- 输出经销商/进口商/客户开发名单时，建议增加字段：`X线索`、`账号/帖子链接`、`线索类型`、`时间`、`置信度`、`需验证事项`。

边界要求：

- 只检索公开内容；不登录、不绕过访问限制。
- 不自动关注、点赞、评论、转发、私信。
- 如需使用用户账号、发送消息或进行任何外部互动，必须先向用户确认。

#### Facebook 公开信息搜索

当外贸市场调研进入海外客户开发、经销商核验、门店/仓库/展会活动、区域代理动态、产品促销、WhatsApp/电话线索或本地市场活跃度判断阶段时，使用公开 Facebook 页面作为补充信源。

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
- 输出经销商/进口商/客户开发名单时，建议增加字段：`Facebook线索`、`Facebook主页/帖子链接`、`线索类型`、`最近活跃时间`、`联系方式`、`WhatsApp/电话`、`置信度`、`需验证事项`。

边界要求：

- 只检索公开页面和公开帖子；不登录、不绕过访问限制。
- 不自动点赞、评论、关注、私信、加入群组。
- 如需使用用户账号、发送消息或进行任何外部互动，必须先向用户确认。

### 第五步：输出正式报告

默认报告结构：

```markdown
# [目标国]_[产品]_市场调研报告

## 一、执行摘要
- 核心发现
- 市场机会评级
- 主要进入建议

## 二、市场概况
1. 市场规模与增长趋势
2. 需求驱动因素
3. 主要限制因素
4. 政策、认证、关税或准入要求

## 三、竞争格局
1. 品牌商
2. 制造商
3. 经销商 / 进口商
4. 竞争集中度判断

## 四、重点竞争对手分析

## 五、竞争对手对比矩阵

## 六、价格与渠道分析

## 七、中国供应商进入机会
1. 市场切入点
2. 产品定位建议
3. 价格策略建议
4. 渠道策略建议
5. 本地合作建议

## 八、风险提示
- 合规风险
- 认证风险
- 渠道风险
- 价格竞争风险
- 汇率 / 物流 / 政策风险

## 九、信息来源
```

## 输出保存

如果用户要求保存，使用 `write` 保存到当前工作目录或用户指定目录。

默认文件名：

```text
[目标国]_[产品]_市场调研报告.md
```

例如：

```text
泰国_太阳能板_市场调研报告.md
巴西_液压软管_市场调研报告.md
```

## 子代理拆分建议

深度任务建议这样拆：

- 子任务 1：品牌商列表与基础信息
- 子任务 2：制造商列表与基础信息
- 子任务 3：经销商 / 进口商列表
- 子任务 4：价格、渠道、电商平台验证
- 子任务 5：政策、认证、准入要求
- 主会话：合并、去重、判断、形成报告

每个子代理只返回精炼结果，不返回大量原始网页文本。
