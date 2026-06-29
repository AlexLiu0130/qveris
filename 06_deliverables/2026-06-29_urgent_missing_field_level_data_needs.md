# 美股 AI 产品急需补齐的数据子类目清单

日期：2026-06-29  
版本：v0.1  
用途：用于内部讨论 QVeris 美股 AI 产品下一步数据能力建设与 Discover / Inspect 优先级。

## 一、结论摘要

当前最需要优先补齐的，不是 `open / close / volume` 这类基础行情字段。基础行情在 QVeris 公开资料中已有较明确方向级覆盖。

真正迫切的是：**在投资研究、财报分析、风险监控和 AI 股票差异化分析中必须用到，但目前 QVeris 公开资料尚未字段级确认的数据子类目。**

这里的“目前还没有”采用谨慎口径：

- 不是断言 QVeris 内部一定没有。
- 而是指：基于官网、公开 guide 和公开文档，目前还不能确认到具体字段、tool_id、provider、schema、延迟、覆盖范围和计费规则。
- 下一步需要通过 QVeris `Discover / Inspect` 做字段级确认。

## 二、最迫切的 Top 3

### 1. 分析师预期与市场共识

优先级：P0

急需字段：

- `EPS consensus`
- `Revenue consensus`
- `EBITDA consensus`
- `Free cash flow consensus`
- `Guidance consensus`
- `Target price`
- `Analyst rating`
- `Rating upgrade / downgrade`
- `Estimate revision`
- `Earnings surprise`
- `Revenue surprise`
- `Beat / Miss / In-line`
- `Consensus trend`
- `Dispersion of estimates`

为什么急：

财报分析必须依赖“预期差”。没有共识预期，就无法解释为什么公司业绩看起来不错但股价下跌，或业绩一般但股价上涨。

产品功能：

- 财报预期差分析
- Earnings monitor
- Analyst revision alert
- 财报后股价反应解释
- 个股研究 Agent 的核心判断模块

当前 QVeris 状态：

QVeris 公开资料已经提到 investment research、earnings analysis、analyst consensus 等方向，但尚未从公开资料确认到上述字段级 schema。因此应列为第一批 Inspect 对象。

## 三、按优先级列出的急需字段

| 优先级 | 数据大类 | 急需子类目 / 字段级数据 | 当前公开确认状态 | 为什么重要 |
|---|---|---|---|---|
| P0 | 分析师预期与市场共识 | `EPS consensus`、`Revenue consensus`、`EBITDA consensus`、`FCF consensus`、`target price`、`rating`、`upgrade/downgrade`、`estimate revision`、`earnings surprise`、`beat/miss/in-line` | 方向级提到，字段级待 Inspect | 财报分析和预期差判断必需 |
| P0 | 宏观经济与利率 | `Fed Funds Rate`、`2Y yield`、`10Y yield`、`yield curve`、`CPI`、`PCE`、`Core CPI`、`Core PCE`、`FOMC calendar`、`FOMC statement` | 方向级提到 macro，字段级待 Inspect | AI/成长股估值高度受利率影响 |
| P0/P1 | 估值增强 | `Forward P/E`、`EV/Sales`、`EV/EBITDA`、`FCF Yield`、`historical valuation range`、`valuation percentile`、`peer comparison`、`sector valuation`、`implied growth rate` | 部分可由行情和基本面计算，字段级待确认 | 公司研究和估值助手必需 |
| P1 | 期权与波动率 | `options chain`、`open interest`、`implied volatility`、`IV Rank`、`put/call ratio`、`expected move`、`unusual options activity`、`gamma exposure`、`skew`、`term structure` | 公开资料提到 options，字段级待 Inspect | 财报前后波动、风险定价和市场情绪判断 |
| P1 | 资金流与持仓 | `ETF flows`、`sector fund flows`、`institutional ownership`、`13F holdings`、`insider transactions`、`buyback data`、`hedge fund positioning`、`retail flow` | 公开资料未充分字段级确认 | 判断资金流向、机构偏好和交易拥挤度 |
| P1 | 做空与卖空 | `short interest`、`days to cover`、`short volume`、`borrow fee`、`shares available to borrow`、`securities lending utilization`、`fail to deliver` | 公开资料未确认 | 热门 AI 股、小盘股、meme stocks 的风险预警必需 |
| P1/P2 | 高级微观结构 | `Level 2 order book`、`market depth`、`order imbalance`、`auction imbalance`、`venue distribution`、`TRF reported trades` | 基础 trades/quotes 有方向级线索，高级字段待 Inspect | 判断交易质量、盘口压力和机构交易结构 |
| P2 | AI 供应链 | `GPU orders`、`HBM supply/demand`、`CoWoS capacity`、`AI server shipment`、`cloud capex`、`hyperscaler capex`、`data center pipeline`、`power capacity`、`lead time`、`backlog` | 公开资料未确认 | QVeris 美股 AI 产品的关键差异化数据层 |
| P2 | Dark Pool / Block / Off-exchange | `dark pool volume`、`ATS volume`、`off-exchange volume`、`block trades`、`large trade prints`、`TRF trades`、`ATS market share` | 公开资料未确认 | 观察机构大额交易、场外流动性和隐藏交易结构 |

## 四、建议的 Inspect 顺序

### 第一批：必须马上确认

1. `analyst estimates consensus EPS revenue target price rating revisions`
2. `earnings surprise beat miss revenue surprise guidance consensus`
3. `FRED macro data treasury yields CPI PCE FOMC calendar`
4. `valuation ratios historical valuation percentile peer comparison US equities`

### 第二批：专业增强能力

1. `options chain implied volatility open interest expected move put call ratio`
2. `ETF flows institutional ownership 13F insider transactions buybacks`
3. `short interest short volume borrow fee fail to deliver`
4. `Level 2 order book market depth order imbalance US equities`

### 第三批：差异化能力

1. `AI supply chain GPU HBM CoWoS cloud capex data center construction`
2. `semiconductor equipment orders AI server shipments optical module demand`
3. `dark pool ATS TRF block trades off exchange volume US equities`

## 五、产品落地含义

### MVP 不能缺

- 分析师预期与财报 surprise
- 核心宏观利率
- 基础估值增强

这些决定产品能不能完成“靠谱的个股研究和财报解释”。

### 专业版要补

- 期权波动率
- 资金流与机构持仓
- 做空与卖空
- 高级微观结构

这些决定产品能不能服务更专业的交易和风险分析。

### 差异化要押注

- AI 供应链
- Cloud / hyperscaler capex
- Dark pool / block / off-exchange

这些决定产品是不是只是普通股票工具，还是一个真正面向 AI 投资研究的产品。

## 六、公开资料依据

QVeris 公开资料显示，其 finance capabilities 已覆盖或提到以下方向：

- market data
- fundamentals
- earnings data
- analyst consensus
- valuation models
- macro research
- options
- crypto
- risk and compliance
- alternative signals

但公开资料通常是方向级描述，并不等于字段级可用。因此上述清单仍需要通过 `Discover / Inspect` 做最终确认。

参考链接：

- QVeris Finance AI Agent Tools: https://qveris.ai/guides/finance-capabilities/
- QVeris AI Earnings Analysis Agent: https://qveris.ai/guides/ai-earnings-analysis-agent/
- QVeris MCP Server List for Finance: https://qveris.ai/guides/mcp-server-list-finance/
- QVeris MCP Server Integration Guide: https://qveris.ai/guides/mcp-server-integration-guide/

