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

## 海关数据 / 贸易数据强制纳入

外贸市场调研、竞品分析、客户开发、供应商/企业背调、目标国进口商/经销商识别时，必须默认把海关数据/贸易数据作为独立证据层纳入，而不是只查官网、B2B 和社媒。

### 必做动作

1. **单列调研维度**：报告中必须包含“海关数据/贸易数据”小节。
2. **主动尝试检索**：围绕公司名、品牌名、产品英文名、目标国、HS Code、进口商/经销商、竞品供应商做查询。
3. **优先使用用户数据**：如果用户提供已购买的海关数据、Excel、CSV、截图或导出记录，优先读取并用于客户筛选、竞品客户挖掘和采购规律分析。
4. **公开数据尽力覆盖**：没有用户数据时，尽力检索公开海关/贸易数据库、进口商目录、B2B 交易线索、提单/航运/贸易记录摘要、采购商名录。
5. **缺失也要写明**：如果无法获取，不能省略该维度，必须标注“海关数据缺失/待验证”，并说明对结论的影响。
6. **权限边界**：不绕过付费墙、登录墙、验证码或权限限制；付费库和用户私有数据必须在用户授权或提供后使用。

### 查询模板

```text
"[Company Name]" import export records
"[Company Name]" customs data
"[Company Name]" bill of lading
"[Brand]" shipment records
"[Product]" "[Country]" importers
"[HS Code]" "[Country]" importers distributors
"[Competitor]" customer import records
"[中文公司名]" 海关数据
"[中文公司名]" 出口 进口商
"[中文公司名]" 提单
```

### 输出字段建议

```text
海关数据/贸易数据：已获取/公开线索/缺失待验证
相关 HS Code：
目标国进口商/采购商线索：
交易频次/出货量/金额：
竞品客户线索：
数据来源与时间范围：
限制说明：
对结论影响：
```

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
- 海关数据/贸易线索
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
- 海关数据 / 贸易数据库 / 进口商目录 / 交易线索
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

- 尽可能获取 LinkedIn 公司页、人员页、岗位、地区、动态、互动、关联公司等信息。
- 如遇登录后可见内容、更多人员列表、联系人导出、消息互动等情况，先记录到“待登录清单”，不中断当前调研；报告出完后单独提醒用户，经同意后再登录补采。
- 输出经销商/进口商/客户开发名单时，建议增加字段：`LinkedIn线索`、`可能联系人/角色`、`职位`、`公开链接`、`登录后可补充项`、`置信度`、`备注`。

#### X / Twitter 公开信息搜索

当外贸市场调研进入市场热度、客户声音、品牌口碑、展会活动、经销商动态、采购线索、招聘扩张或实时事件验证阶段时，使用 X/Twitter 公开信息作为补充信源。

优先工具：

- `grok_search` with `platform: "Twitter"`：优先用于补充实时讨论、趋势和平台内语义搜索；如遇 403/503/超时等错误，间隔约 2 秒重试，最多重试 2 遍；仍失败再降级到 `site:x.com` / `site:twitter.com`、Tavily、dual_search。
- `tavily_search` / `dual_search` / `web_search`：搜索 `site:x.com` 或 `site:twitter.com` 公开页面。
- `exa_search`：不要再使用已废弃的 tweet 分类；可不指定 category，作为普通语义搜索补充。
- `browser`：必要时打开 X/Twitter 页面做可视化验证；如页面要求登录或出现访问限制，先记入待登录清单，报告出完后提醒用户是否登录补采。
- `@xquik/tweetclaw` OpenClaw 插件（可选）：当当前 workspace 已安装并允许 `explore` / `tweetclaw` 工具时，只把它用于 X/Twitter 公开信源补充，例如 tweet 搜索、回复检索、用户公开资料、followers/following 公开线索和用户公开时间线。先用 `explore` 确认只读 endpoint，再用 `tweetclaw` 记录查询词、endpoint、时间范围、公开链接和置信度。

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

登录后置提醒：

- 遇到登录后可见的账号、帖子、评论、互动、粉丝/关注列表、搜索结果时，先记录到“待登录清单”。
- 报告出完后单独提醒用户：哪些 X/Twitter 内容需要登录、登录后预计能补充哪些信息；经用户同意后再登录补采。
- 使用 TweetClaw 时，不把发帖、回复、私信、媒体上传/下载、monitor、webhook 或其他账号操作放进本 skill 的默认流程；如用户需要这些动作，另开明确的 TweetClaw/OpenClaw 流程并等待确认。

#### Facebook 公开信息搜索

当外贸市场调研进入海外客户开发、经销商核验、门店/仓库/展会活动、区域代理动态、产品促销、WhatsApp/电话线索或本地市场活跃度判断阶段时，使用公开 Facebook 页面作为补充信源。

Facebook 没有专用 `exa_search` category，优先通过域名限定和普通网页搜索完成：

- `tavily_search` / `dual_search` / `web_search`：搜索 `site:facebook.com` 公开页面。
- `exa_search`：不指定 category，使用普通语义搜索补充。
- `browser`：打开 Facebook 页面做可视化验证；如页面要求登录或出现访问限制，先记入待登录清单，报告出完后提醒用户是否登录补采。

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

登录后置提醒：

- 遇到登录后可见的主页、帖子、评论、群组、联系方式、互动列表时，先记录到“待登录清单”。
- 报告出完后单独提醒用户：哪些 Facebook 内容需要登录、登录后预计能补充哪些信息；经用户同意后再登录补采。

#### Instagram 公开信息搜索

当外贸调研进入品牌曝光、产品图片、展会活动、经销商/门店线索、客户使用场景判断时，补充 Instagram。

优先工具：`tavily_search` / `dual_search` / `web_search` 的 `site:instagram.com`，必要时 `browser` 可视化验证。

查询示例：

```text
site:instagram.com "[Company Name]"
site:instagram.com "[Brand]" "[Product]"
site:instagram.com "[Product]" "[Country]" distributor
"[Company Name]" Instagram
"[Brand]" Instagram hydraulic hose
```

输出字段建议：`Instagram线索`、`主页/帖子链接`、`内容类型`、`最近活跃时间`、`产品/展会/客户场景`、`登录后可补充项`、`置信度`、`需验证事项`。

#### YouTube / TikTok 视频平台搜索

当需要判断工厂展示、产品测试、安装演示、展会现场、客户案例、品牌传播活跃度时，补充 YouTube / TikTok。

查询示例：

```text
site:youtube.com "[Company Name]" "[Product]"
site:youtube.com "[Brand]" hydraulic hose
site:tiktok.com "[Company Name]"
site:tiktok.com "[Product]" "[Country]"
"[Company Name]" factory video
"[Brand]" product demo
```

输出字段建议：`视频线索`、`平台`、`视频链接`、`视频主题`、`发布时间`、`能否佐证真实经营/产品能力`、`登录后可补充项`、`置信度`。

#### 微信公众号 / 中文社媒搜索

当调研中国供应商、竞品、制造企业主体口径、认证荣誉、展会活动、招聘扩张、政府项目、党建/企业动态时，补充微信公众号、抖音、视频号、小红书、B站等中文社媒。

查询示例：

```text
"[中文公司名]" 微信公众号
"[中文公司名]" 公众号 展会
"[中文公司名]" 认证 公众号
"[中文公司名]" 招聘
"[中文公司名]" 抖音
"[中文公司名]" 视频号
"[中文公司名]" 小红书
"[中文公司名]" B站
```

输出字段建议：`中文社媒线索`、`平台`、`账号/文章/视频链接`、`国内宣传口径`、`认证/荣誉/展会/招聘信息`、`与海外平台口径是否一致`、`登录后可补充项`、`置信度`。

#### Reddit / Quora / 行业论坛口碑搜索

当需要判断产品口碑、投诉、使用反馈、维修问题、采购讨论、品牌被提及时，补充 Reddit / Quora / 行业论坛。

查询示例：

```text
site:reddit.com "[Brand]" "[Product]"
site:reddit.com "hydraulic hose" "[Brand]"
site:quora.com "[Product]" "[Brand]"
"[Brand]" complaint forum
"[Product]" forum "[Country]"
```

输出字段建议：`口碑线索`、`平台/论坛`、`链接`、`讨论主题`、`正负面倾向`、`是否有第二来源`、`待核验事项`。

#### 社媒与职业网络统一判断

- 输出分层术语统一使用：`已验证事实 / 平台公开口径 / 社媒线索 / 推测判断 / 待核验项`。
- 社媒信息作为客户开发、渠道判断、活跃度判断、风险识别的重要线索；负面信息、投诉、传言类内容应尽量交叉验证或列为待核验。
- 遇到需要登录才能查看的主页、帖子、评论、人员列表、联系方式、群组或视频互动，先纳入“待登录清单”；报告出完后单独提醒用户，经同意后再登录补采。

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

## 七、社媒与职业网络分析
1. LinkedIn 职业网络线索
2. Facebook / Instagram 公开社媒线索
3. X/Twitter 公开讨论
4. YouTube / TikTok 视频线索
5. 微信公众号 / 中文社媒线索
6. Reddit / Quora / 行业论坛口碑线索
7. 社媒可信度与待登录补采清单

## 八、中国供应商进入机会
1. 市场切入点
2. 产品定位建议
3. 价格策略建议
4. 渠道策略建议
5. 本地合作建议

## 九、风险提示
- 合规风险
- 认证风险
- 渠道风险
- 价格竞争风险
- 汇率 / 物流 / 政策风险

## 十、信息来源

## 十一、待登录补采清单
- 需要登录的平台/网站：
- 登录后预计可补充的信息：
- 是否建议登录补采：
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
