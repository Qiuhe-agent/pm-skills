# Claude Code for 新媒体运营 - 产品需求文档 (PRD)

**产品名称**：Claude Code for Content（暂定名：Claude Content）
**版本**：v1.0 (MVP)
**日期**：2026-03-16
**状态**：概念验证 → 开发就绪

---

## 目录
1. [产品概览](#1-产品概览)
2. [目标用户与痛点](#2-目标用户与痛点)
3. [核心功能详细规格](#3-核心功能详细规格)
4. [技术架构设计](#4-技术架构设计)
5. [数据模型](#5-数据模型)
6. [API 设计](#6-api-设计)
7. [用户故事与验收标准](#7-用户故事与验收标准)
8. [冲刺计划](#8-冲刺计划)
9. [测试策略](#9-测试策略)
10. [监控与指标](#10-监控与指标)
11. [风险与依赖](#11-风险与依赖)

---

## 1. 产品概览

### 1.1 产品愿景
> **"让每一位内容创作者都拥有一位 24/7 的智能内容运营伙伴，释放创造力，专注于真正重要的事。"**

### 1.2 核心定位
**Claude Content** - 不只是 AI 写作工具，而是**全栈新媒体运营伙伴**：
- 理解你的品牌调性和历史内容，而非从零开始
- 执行多步骤运营工作流，而非单次生成
- 连接多平台数据，而非单平台工具
- 人类始终拥有最终创意控制权

### 1.3 为什么是现在？

| 趋势 | 机会 |
|------|------|
| **内容平台碎片化** | 公众号、小红书、抖音、B站、微博... 需要多平台运营 |
| **内容生产压力大** | 日更、周更、多体裁（图文/短视频/直播脚本） |
| **数据分散** | 每个平台数据独立，难以全局分析 |
| **AI 写作工具泛滥但浅** | 大多是单次生成，不理解品牌和历史 |
| **运营工作重复繁琐** | 回复评论、整理素材、排版格式... |

### 1.4 MVP 目标
- 验证核心价值：品牌理解 + 多步骤工作流 + 多平台整合
- 建立早期内容创作者用户基础
- 验证产品主导增长（PLG）策略
- 实现产品市场匹配（PMF）

### 1.5 成功指标（MVP）

| 指标 | 目标 | 测量方式 |
|------|------|---------|
| 试用→付费转化率 | >12% | 计费系统 |
| 周活跃率 | >55% | 产品分析 |
| 月留存率 | >65% | 产品分析 |
| NPS | >45 | 用户调查 |
| 每周节省时间（用户报告） | >6 小时 | 用户调查 |
| 工作流完成率 | >75% | 产品分析 |
| 内容采用率 | >80% | 产品分析 |

---

## 2. 目标用户与痛点

### 2.1 用户分层

| 用户类型 | 描述 | 优先级 |
|---------|------|--------|
| **专业内容运营** | 2-5 年经验，服务品牌或自媒体 | P0 |
| **自媒体创业者** | 1-3 年经验，个人 IP，多平台运营 | P0 |
| **企业品牌运营** | 企业市场部，负责品牌内容 | P1 |
| **内容创作新手** | 刚开始做内容，需要指导和辅助 | P2 |

### 2.2 典型用户画像：小夏

| 属性 | 描述 |
|------|------|
| **姓名** | 小夏 |
| **年龄** | 26 岁 |
| **角色** | 自媒体创业者 + 品牌内容顾问 |
| **经验** | 3 年 |
| **负责平台** | 公众号、小红书、抖音、B站 |
| **粉丝量** | 全网 50 万+ |
| **工作节奏** | 每周 3-4 篇内容，跨平台分发 |
| **工具支出** | 已为 Notion、Canva、剪映等付费 |
| **工作时长** | 每天 8-10 小时，其中 40% 是重复性工作 |

### 2.3 核心痛点（按优先级）

| 痛点 | 量化 | 现有解决方案 | 我们的方案 |
|------|------|-------------|-----------|
| **多平台内容适配耗时** | 30-40% 时间 | 手动改写、复制粘贴 | 一键多平台改写 |
| **回复评论和互动繁琐** | 每天 1-2 小时 | 手动回复、遗漏 | AI 辅助互动 |
| **创意枯竭** | 每周卡壳 2-3 次 | 刷手机、看竞品 | 基于品牌的创意库 |
| **数据分析分散** | 每个平台独立看 | 手动整理 Excel | 统一数据看板 |
| **素材管理混乱** | 找素材花 20 分钟/次 | 文件夹、相册 | 智能素材库 |
| **品牌调性不一致** | 不同人写风格不同 | 冗长的品牌手册 | 品牌理解系统 |

### 2.4 一天的工作流（Before）

```
9:00  起床，刷各平台数据（30 分钟）
      ↓
9:30  回复评论和私信（1 小时）
      ↓
10:30 开选题会，想今天写什么（45 分钟）
      ↓
11:15 开始写公众号长文（2 小时）
      ↓
13:15 午饭 + 休息
      ↓
14:00 改写成小红书版本（45 分钟）
      ↓
14:45 改写成抖音脚本（45 分钟）
      ↓
15:30 找配图、排版（1 小时）
      ↓
16:30 各平台发布，设置定时（30 分钟）
      ↓
17:00 整理本周数据报表（1 小时）
      ↓
18:00 一天结束，感觉没做什么"正事"
```

### 2.5 一天的工作流（After - with Claude Content）

```
9:00  起床，看 Claude 准备的"今日简报"（5 分钟）
      - 各平台数据汇总
      - 高互动评论精选
      - 热点建议
      ↓
9:05  用 Claude 批量回复评论（15 分钟）
      - AI 生成回复草稿
      - 一键确认或修改
      ↓
9:20  从 Claude 的"选题库"选今天的主题（10 分钟）
      - 基于历史高表现内容推荐
      - 结合实时热点
      ↓
9:30  让 Claude 写初稿（15 分钟）
      - 自动符合品牌调性
      - 引用历史内容
      ↓
9:45  人工修改和润色（45 分钟）
      ↓
10:30 一键生成多平台版本（5 分钟）
      - 公众号长文
      - 小红书笔记
      - 抖音脚本
      ↓
10:35 智能配图建议 + 排版（20 分钟）
      ↓
10:55 多平台一键发布（5 分钟）
      ↓
11:00 开始真正的"创意工作" - 策划下个月的大项目！
```

**节省时间：约 4-5 小时/天**

---

## 3. 核心功能详细规格

### 3.1 F1：品牌理解与内容记忆

#### 3.1.1 功能描述
Claude Content 学习你的品牌调性、历史内容风格、受众偏好，所有产出都符合品牌设定。

#### 3.1.2 用户故事
> 作为内容运营，我希望 Claude 理解我们的品牌调性，这样它写的内容就像我自己写的一样。

#### 3.1.3 功能需求

**3.1.3.1 品牌档案建立**
- 品牌基础信息：名称、slogan、使命、价值观
- 目标受众画像：年龄、兴趣、痛点、语言风格
- 品牌声音（Brand Voice）设定：
  - 语气：正式/轻松/幽默/专业
  - 用词偏好：喜欢/避免的词汇
  - 句式风格：短句/长句/问句
  - 视角：第一人称/第三人称
- 视觉风格指南：色彩、字体、配图偏好
- 可配置的品牌约束：不能说的、必须包含的

**品牌档案示例（YAML）：**
```yaml
brand:
  name: "职场充电宝"
  slogan: "每天充电，快速成长"
  voice:
    tone: "friendly, encouraging, practical"
    personality: "像一个靠谱的前辈，温暖但不鸡汤"
    language: "简单易懂，避免术语，多用比喻"
    do:
      - 用"我们"拉近与读者的距离
      - 多给具体的行动建议
      - 用真实的职场案例
    dont:
      - 不要说教
      - 不要用"必须"、"应该"等强势词汇
      - 不要制造焦虑

audience:
  age: "22-35岁"
  role: "职场新人到中层管理者"
  painPoints:
    - "想成长但不知道方法"
    - "职场人际关系复杂"
    - "工作与生活不平衡"

contentRules:
  titleStyle: "数字+痛点/利益点，例如：3个方法让你..."
  structure: "故事开场 → 3个要点 → 总结行动"
  cta: "评论区互动引导，而非生硬的'关注我'"
```

**3.1.3.2 历史内容学习**
- 导入历史内容（公众号文章、小红书笔记等）
- 自动分析内容风格、主题、结构
- 识别高表现内容的特征（阅读、互动）
- 建立内容知识库，可引用和参考
- 增量学习：新内容发布后自动更新理解

**3.1.3.3 受众理解**
- 分析评论和私信，了解受众关心什么
- 识别高频问题和话题
- 学习受众的语言风格（用于互动）
- 发现潜在的内容选题方向

**3.1.3.4 品牌一致性检查**
- 生成内容前的预检查
- 实时提示"这不符合我们的品牌调性"
- 提供修改建议，让内容回归品牌
- 可调整的"品牌严格度"滑块

#### 3.1.4 非功能需求

| 指标 | 目标 |
|------|------|
| 品牌档案配置时间 | < 10 分钟（引导式） |
| 历史内容导入速度 | < 5 分钟（100 篇） |
| 品牌一致性检查 | < 2 秒/篇 |
| 学习效果 | >80% 用户认为"像我写的" |

#### 3.1.5 验收标准

- [ ] 用户可以通过引导式向导建立品牌档案
- [ ] 可以导入历史公众号文章（至少 3 个平台）
- [ ] Claude 生成的内容符合品牌设定的调性
- [ ] 品牌一致性检查能识别不符合的内容
- [ ] 用户认可"这就像我自己写的"（用户测试 >80%）

---

### 3.2 F2：多平台内容工作流

#### 3.2.1 功能描述
一次创作，多平台适配。从一个核心内容，自动生成各平台版本（公众号、小红书、抖音、B站、微博等）。

#### 3.2.2 用户故事
> 作为多平台运营者，我希望写一篇就能发布到所有平台，这样我就不用反复改写了。

#### 3.2.3 功能需求

**3.2.3.1 核心内容创作**
- 支持多种内容输入方式：
  - 完整长文（Markdown/富文本）
  - 要点大纲（bullet points）
  - 语音转文字（录音直接转成内容）
  - 草稿/半成品
- AI 辅助写作：
  - 续写（"帮我继续写"）
  - 扩写（"把这部分写得更详细"）
  - 缩写（"把这篇缩成 500 字"）
  - 改写（"换一种说法"）
- 智能提示：
  - "这里可以加个案例"
  - "这个标题可以更吸引人"
  - "这里需要过渡一下"

**3.2.3.2 平台适配引擎**
- 预设各平台模板：

| 平台 | 特点 | 长度 | 风格 |
|------|------|------|------|
| **公众号** | 深度长文 | 1500-3000 字 | 正式、完整、有逻辑 |
| **小红书** | 笔记/干货 | 300-800 字 | 轻松、 emoji、分段清晰 |
| **抖音** | 短视频脚本 | 30-60 秒 | 口语化、有钩子、有金句 |
| **B站** | 中视频脚本 | 5-10 分钟 | 详细、有梗、互动性 |
| **微博** | 短内容 | 140-300 字 | 话题、热点、互动 |
| **知乎** | 问答/专栏 | 1000-2000 字 | 专业、可信、有引用 |

- 一键生成所有平台版本
- 可选择要生成的平台
- 每个平台版本可以单独编辑
- 保留原始引用（方便追溯）

**平台适配示例：**

```
【原始内容 - 公众号长文】
标题：3个方法，让你从"职场透明人"变"不可替代"
（2500字，详细阐述3个方法，每个方法都有案例和行动建议）

【小红书版本 - 自动生成】
✨ 3个方法让你职场逆袭，从透明人到不可替代！

😭 有没有过这种经历：
- 开会总是坐角落
- 好事轮不到你
- 辛苦干活却没人看见

今天分享3个亲测有效的方法：

1️⃣ 「成果可视化」
不要只埋头干活，要让别人看见！
👉 每周发周报，用数据说话
👉 项目结束后做复盘总结

2️⃣ 「打造个人标签」
让别人想到某件事就想到你！
👉 找到你的差异化优势
👉 主动承接相关任务

3️⃣ 「建立人脉银行」
职场不是单打独斗！
👉 每周和1个同事喝咖啡
👉 主动帮助别人

💡 记住：职场不是比谁更努力，而是比谁更有策略！

你是职场透明人吗？评论区聊聊～

#职场 #职场干货 #个人成长 #职场技巧

【抖音脚本 - 自动生成】
[0-3s] 画面：坐在角落，没人理
      台词：你是职场透明人吗？

[3-8s] 画面：快速闪回
      台词：开会没人听你说话
             好事轮不到你
             辛苦干活却被忽略

[8-15s] 画面：坐正，面对镜头
      台词：今天分享3个方法，让你从透明人变不可替代

[15-30s] 画面：字幕+动作
      台词：第一个，成果可视化！
             不要只埋头干
             每周发周报，用数据说话
             项目结束做个复盘

[30-45s] 画面：第二个方法
      台词：第二个，打造个人标签！
             让别人想到某件事就想到你
             找到你的差异化优势
             主动承接相关任务

[45-60s] 画面：第三个方法+总结
      台词：第三个，建立人脉银行！
             每周和1个同事聊聊天
             主动帮助别人
             记住，职场不是比谁更努力
             而是比谁更有策略！

[60-65s] 画面：指向评论区
      台词：你是职场透明人吗？评论区聊聊！
      字幕：关注我，每天一个职场干货
```

**3.2.3.3 内容日历与定时发布**
- 内容日历视图（周/月）
- 拖拽安排发布时间
- 各平台发布时间建议（基于历史数据）
- 定时发布（无需值守）
- 发布状态实时跟踪

**3.2.3.4 A/B 测试支持**
- 同一个内容生成 2-3 个版本
- 同时发布到不同平台/分组
- 自动跟踪表现
- 推荐最优版本

#### 3.2.4 非功能需求

| 指标 | 目标 |
|------|------|
| 多平台生成时间 | < 10 秒（5 个平台） |
| 内容质量评分 | > 4.2/5（用户评分） |
| 平台适配准确率 | > 85%（无需大改） |

#### 3.2.5 验收标准

- [ ] 用户可以输入一篇长文，一键生成 5 个平台版本
- [ ] 每个平台版本符合该平台的风格和长度
- [ ] 内容日历可以拖拽安排发布时间
- [ ] 定时发布功能正常工作
- [ ] 用户认为"基本不用改就能用"（>80%）

---

### 3.3 F3：智能互动助手

#### 3.3.1 功能描述
AI 辅助回复评论、私信，保持品牌调性，筛选高价值互动。

#### 3.3.2 用户故事
> 作为内容运营，我希望 AI 帮我处理评论和私信，这样我就能专注于真正需要我的互动。

#### 3.3.3 功能需求

**3.3.3.1 评论聚合与分类**
- 聚合所有平台的评论和私信
- 智能分类：
  - 提问（需要回答）
  - 赞美（感谢即可）
  - 批评（需要认真处理）
  - 灌水/广告（可以忽略）
  - 合作邀约（转给商务）
- 优先级排序：
  - 高赞评论（前排）
  - 粉丝提问（潜在深度互动）
  - 负面评论（需要快速响应）

**3.3.3.2 AI 回复生成**
- 基于品牌调性生成回复草稿
- 多种回复风格可选：
  - 正式
  - 亲切
  - 幽默
  - 简洁
- 一键确认发布
- 回复历史学习（越用越像你）

**回复示例：**

```
【用户评论】
"这篇太实用了！能不能出一期关于职场沟通的？"

【AI 生成的回复选项】

[亲切版] ✨
"谢谢你的喜欢！职场沟通已经在我的选题库里了，
敬请期待～ 还有什么想看的随时告诉我！"

[简洁版]
"感谢支持！职场沟通安排上了，关注更新～"

[互动版]
"开心你喜欢！职场沟通是个好话题，
你最想了解沟通的哪方面呢？"

→ 用户选择一个，一键发布
```

**3.3.3.3 批量处理**
- "一键感谢所有赞美"
- "一键回答常见问题"（基于知识库）
- "批量点赞高价值评论"
- 可选择"处理所有已审核的"

**3.3.3.4 互动洞察**
- 评论热词云图
- 高频问题汇总
- 受众情绪分析
- 互动建议："这个话题大家很关心，可以再写一篇"

**3.3.3.5 评论管理规则**
- 自动隐藏/删除广告评论
- 敏感词过滤
- 自动回复设置（"首次关注自动回复"）
- 黑名单管理

#### 3.3.4 非功能需求

| 指标 | 目标 |
|------|------|
| 评论聚合延迟 | < 5 分钟 |
| 分类准确率 | > 90% |
| 回复生成时间 | < 2 秒/条 |
| 回复采用率 | > 75% |

#### 3.3.5 验收标准

- [ ] 所有平台的评论都能聚合到一个地方
- [ ] 评论能正确分类（提问/赞美/批评等）
- [ ] AI 生成的回复符合品牌调性
- [ ] 可以批量处理评论
- [ ] 用户觉得"节省了大量时间"（>80%）

---

### 3.4 F4：统一数据看板与洞察

#### 3.4.1 功能描述
连接所有平台的数据，统一展示，提供智能洞察和建议。

#### 3.4.2 用户故事
> 作为内容运营，我希望在一个地方看到所有平台的数据，这样我就不用一个个去看了。

#### 3.4.3 功能需求

**3.4.3.1 多平台数据聚合**
- 支持的平台：
  - 公众号（阅读、在看、分享、收藏）
  - 小红书（阅读、点赞、收藏、评论）
  - 抖音（播放、点赞、评论、转发、完播率）
  - B站（播放、弹幕、点赞、收藏、投币）
  - 微博（阅读、转发、评论、点赞）
- 数据自动同步（每天/每小时）
- 历史数据导入（可选）

**3.4.3.2 统一数据看板**

**今日概览：**
```
┌─────────────────────────────────────────────────────────────┐
│  今日简报  2026-03-16  星期一                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📊 数据总览                                                │
│  ┌──────────┬──────────┬──────────┬──────────┐           │
│  │  总阅读  │  总互动  │  新增粉丝 │  点击率  │           │
│  │  128.5k  │   8.2k   │   3,241  │  6.4%    │           │
│  └──────────┴──────────┴──────────┴──────────┘           │
│                                                              │
│  🚀 最佳表现                                                │
│  • 《3个方法让你职场逆袭》- 小红书 5.2k 赞                │
│  • 《职场新人必看》- 抖音 120k 播放                       │
│                                                              │
│  💡 智能建议                                                │
│  • 职场话题表现很好，可以继续深耕                           │
│  • 抖音晚 8 点发布效果最好                                 │
│  • "方法"类标题点击率高                                     │
│                                                              │
│  🔔 需要关注                                                │
│  • 有 3 条高赞评论等待回复                                 │
│  • 昨天的推文数据低于平均，建议复盘                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**详细指标：**
- 内容表现表格（可排序、筛选）
- 趋势图（日/周/月）
- 平台对比
- 内容类型对比（图文/视频）

**3.4.3.3 智能洞察**
- 自动发现规律：
  - "你在小红书的最佳发布时间是周三晚 8 点"
  - "带数字的标题点击率高出 40%"
  - "3-5 分钟的视频完播率最高"
  - "职场类内容粉丝转化率最高"
- 选题建议：
  - 基于历史高表现内容推荐
  - 结合实时热点
  - 基于评论区问题
- 竞品对比（可选）：
  - 监控竞品表现
  - 发现竞品的爆款主题

**3.4.3.4 自定义报表**
- 拖拽式报表生成
- 预设报表模板：
  - 周报（给老板）
  - 内容复盘
  - 增长报告
- 一键导出（PDF/Excel/PPT）

#### 3.4.4 非功能需求

| 指标 | 目标 |
|------|------|
| 数据同步延迟 | < 1 小时 |
| 看板加载时间 | < 3 秒 |
| 洞察生成时间 | < 10 秒 |
| 数据准确率 | > 99% |

#### 3.4.5 验收标准

- [ ] 5 个主要平台的数据都能聚合
- [ ] 今日简报清晰展示关键数据
- [ ] 智能洞察能发现有价值的规律
- [ ] 周报可以一键导出
- [ ] 用户觉得"数据清楚多了"（>85%）

---

### 3.5 F5：素材库与知识管理

#### 3.5.1 功能描述
智能管理图片、视频、文案、模板，快速找到需要的素材。

#### 3.5.2 用户故事
> 作为内容运营，我希望快速找到我需要的素材，这样我就不用在文件夹里翻半天了。

#### 3.5.3 功能需求

**3.5.3.1 智能素材库**
- 支持的素材类型：
  - 图片（JPG、PNG、GIF、WebP）
  - 视频（MP4、MOV）
  - 文案片段（Markdown）
  - 模板（内容模板、封面模板）
- 自动标签和分类：
  - AI 自动识别图片内容
  - 提取文案关键词
  - 基于使用场景分类
- 智能搜索：
  - 自然语言搜索："找一张职场开会的图片"
  - 相似图片搜索
  - 按颜色、风格筛选
- 一键插入到内容中

**3.5.3.2 内容模板库**
- 预设模板：
  - 公众号文章结构模板
  - 小红书笔记模板
  - 抖音脚本模板
  - 标题模板（100+）
- 自定义模板：
  - 保存常用结构作为模板
  - 带变量占位符：`{{标题}}`、`{{案例}}`
- 模板市场（后续版本）

**标题模板示例：**
```
数字类：
- X个方法，让你...
- X种人，一定要...
- 这X件事，改变了我...

痛点类：
- 你是不是也...？
- 为什么你总是...？
- 别再...了！

利益类：
- 一文讲透...
- 我用这个方法，...
- 从...到...，我做对了什么

对话类：
- "..."
- 我：... 朋友：...
```

**3.5.3.3 知识管理**
- 品牌知识库：
  - 常见问题及答案
  - 产品/服务介绍
  - 创始人故事
  - 数据和案例
- 引用功能：
  - 写内容时一键引用知识库
  - 确保信息准确一致
- 版本历史：
  - 知识库变更历史
  - 可回滚到之前版本

**3.5.3.4 配图助手**
- 为内容智能推荐配图：
  - 分析内容主题
  - 推荐相关图片
  - 支持免费图库集成（Unsplash、Pexels）
  - 支持企业自有图库
- 封面生成：
  - 一键生成各平台封面
  - 品牌模板自动应用
  - 可自定义调整

#### 3.5.4 非功能需求

| 指标 | 目标 |
|------|------|
| 素材搜索响应 | < 1 秒 |
| 标签准确率 | > 85% |
| 存储空间 | 10GB（基础版） |
| 素材上传速度 | < 5 秒/张 |

#### 3.5.5 验收标准

- [ ] 可以上传和管理图片、视频、文案
- [ ] AI 能自动给素材打标签
- [ ] 可以用自然语言搜索素材
- [ ] 标题模板库能提供有用的建议
- [ ] 用户觉得"找素材快多了"（>80%）

---

### 3.6 F6：跨平台支持（Web + 移动端）

#### 3.6.1 功能描述
Web 端深度工作，移动端快捷处理，随时随地管理内容。

#### 3.6.2 用户故事
> 作为内容运营，我希望在手机上也能快速处理评论和看数据，这样我就不用总守在电脑前了。

#### 3.6.3 功能需求

**3.6.3.1 Web 端（主界面）**
- 完整功能：
  - 内容创作（大屏编辑）
  - 数据看板（详细分析）
  - 素材管理（拖拽上传）
  - 品牌配置（详细设置）
- 多窗口支持：
  - 内容编辑 + 数据看板
  - 素材库 + 内容预览
- 快捷键支持：
  - `Cmd/Ctrl + K`：快速搜索
  - `Cmd/Ctrl + Enter`：发布
  - `/`：唤起命令面板

**3.6.3.2 移动端（App/小程序）**
- 核心场景：
  - 查看数据和今日简报
  - 回复评论和私信
  - 快速记录灵感
  - 审批内容（团队版）
  - 接收通知（数据预警、评论提醒）
- 移动端优化：
  - 语音输入灵感
  - 快捷回复模板
  - 手势操作

**移动端界面示例：**
```
┌─────────────────┐
│ 📱 Claude Content │
├─────────────────┤
│ [ 今日简报 ]    │
│ • 阅读 128.5k   │
│ • 互动 8.2k     │
│ • 新粉 3,241    │
│                 │
│ [ 待处理 ]  3   │
│ • 高赞评论      │
│ • 私信          │
│ • 内容审批      │
│                 │
│ [ 快捷操作 ]    │
│ [✍️ 记录灵感]    │
│ [📊 看数据]     │
│ [💬 回评论]     │
└─────────────────┘
```

**3.6.3.3 统一体验**
- 数据实时同步
-  draft 自动保存和同步
- 操作历史跨平台
- 通知跨平台（Web 端弹窗、移动端推送）

#### 3.6.4 非功能需求

| 指标 | 目标 |
|------|------|
| Web 端加载 | < 2 秒 |
| 移动端启动 | < 1.5 秒 |
| 数据同步延迟 | < 5 秒 |
| 离线可用 | 移动端核心功能可用 |

#### 3.6.5 验收标准

- [ ] Web 端所有功能可用
- [ ] 移动端可以查看数据和回复评论
- [ ] 数据在两端实时同步
- [ ] 移动端离线也能记录灵感
- [ ] 用户觉得"手机上处理很方便"（>80%）

---

## 4. 技术架构设计

### 4.1 系统概览

```
┌─────────────────────────────────────────────────────────────────┐
│                        用户界面层 (UI Layer)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │   Web 应用    │  │  移动端 App   │  │  浏览器插件   │        │
│  │  (React)     │  │  (React Native)│  │  (Chrome)    │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                      应用逻辑层 (App Logic Layer)                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  内容编辑器   │  │  平台适配引擎  │  │  品牌理解系统  │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  评论助手     │  │  数据看板     │  │  素材管理     │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  工作流引擎   │  │  洞察生成器   │  │  发布调度器   │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                   平台集成层 (Platform Integration Layer)         │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐         │
│  │公众号│ │小红书│ │ 抖音 │ │ B站 │ │ 微博 │ │ 知乎 │         │
│  │ API │ │ API │ │ API │ │ API │ │ API │ │ API │         │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘         │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                        AI 模型层 (AI Model Layer)                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │           Claude 大语言模型（通过 Anthropic API）            │ │
│  │  • Claude 3.5 Sonnet（默认：内容创作）                       │ │
│  │  • Claude 3.5 Haiku（快速回复、实时处理）                    │ │
│  │  • Claude 3.5 Opus（深度分析、洞察生成）                     │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                 专用模型（可选）                              │ │
│  │  • 图片理解（理解素材内容）                                   │ │
│  │  • 情感分析（评论情绪）                                       │ │
│  │  • 语音转文字（移动端）                                       │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                        数据存储层 (Data Layer)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  PostgreSQL  │  │  对象存储     │  │  搜索引擎     │        │
│  │  (主数据库)   │  │  (S3/素材)    │  │  (Elasticsearch)│        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
│  ┌──────────────┐  ┌──────────────┐                            │
│  │  Redis 缓存  │  │  向量数据库   │                            │
│  │  (会话/热点)  │  │  (内容相似性)  │                            │
│  └──────────────┘  └──────────────┘                            │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 关键技术决策

| 决策项 | 选择 | 理由 | 备选方案 |
|--------|------|------|---------|
| 前端语言 | TypeScript | 类型安全、生态成熟 | JavaScript |
| Web 框架 | Next.js | SSR、SEO、全栈能力 | React、Vue |
| 移动端 | React Native | 跨平台、代码复用 | Flutter、原生 |
| 后端框架 | NestJS | TypeScript、模块化、可扩展 | Express、Go |
| 主数据库 | PostgreSQL | 关系型、事务支持、成熟 | MySQL |
| 搜索引擎 | Elasticsearch | 全文搜索、强大 | Meilisearch |
| 向量数据库 | Pinecone | 托管、易用 | Weaviate、pgvector |
| 缓存 | Redis | 高性能、丰富数据结构 | Memcached |
| 对象存储 | S3（兼容） | 成熟、低成本 | 阿里云 OSS |
| AI 模型 | Claude 3.5 Sonnet | 长文本、创意写作 | GPT-4 |
| 消息队列 | BullMQ | 可靠、延迟任务 | RabbitMQ |

### 4.3 目录结构

```
claude-content/
├── apps/
│   ├── web/                      # Web 应用
│   │   ├── src/
│   │   │   ├── pages/            # 页面
│   │   │   ├── components/       # 组件
│   │   │   ├── hooks/            # React hooks
│   │   │   ├── lib/              # 工具
│   │   │   └── ...
│   │   └── package.json
│   │
│   ├── mobile/                   # 移动端应用
│   │   ├── src/
│   │   │   ├── screens/          # 屏幕
│   │   │   ├── components/       # 组件
│   │   │   └── ...
│   │   └── package.json
│   │
│   └── api/                      # 后端 API
│       ├── src/
│       │   ├── modules/          # 业务模块
│       │   │   ├── content/      # 内容模块
│       │   │   ├── brand/        # 品牌理解
│       │   │   ├── platform/     # 平台集成
│       │   │   ├── analytics/    # 数据分析
│       │   │   ├── engagement/   # 互动助手
│       │   │   └── media/        # 素材管理
│       │   ├── ai/               # AI 相关
│       │   │   ├── prompts/      # 提示词模板
│       │   │   └── clients/      # AI 客户端
│       │   ├── jobs/             # 后台任务
│       │   └── ...
│       └── package.json
│
├── packages/
│   ├── shared/                   # 共享代码
│   │   ├── src/
│   │   │   ├── types/            # 类型定义
│   │   │   ├── utils/            # 工具函数
│   │   │   └── constants/        # 常量
│   │   └── package.json
│   │
│   ├── platform-apis/            # 平台 API 封装
│   │   ├── src/
│   │   │   ├── wechat/           # 公众号
│   │   │   ├── xiaohongshu/      # 小红书
│   │   │   ├── douyin/           # 抖音
│   │   │   └── ...
│   │   └── package.json
│   │
│   └── ai-sdk/                   # AI SDK 封装
│       ├── src/
│       │   ├── content/          # 内容生成
│       │   ├── brand/            # 品牌理解
│       │   ├── analysis/         # 数据分析
│       │   └── ...
│       └── package.json
│
├── infra/                        # 基础设施
│   ├── terraform/                # Terraform 配置
│   └── docker/                   # Docker 配置
│
├── docs/                         # 文档
├── scripts/                      # 脚本
└── package.json (monorepo)
```

---

## 5. 数据模型

### 5.1 核心表结构

#### users（用户表）
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  avatar_url TEXT,
  timezone TEXT DEFAULT 'Asia/Shanghai',
  plan TEXT DEFAULT 'free', -- free, pro, team, enterprise
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB
);
```

#### brands（品牌表）
```sql
CREATE TABLE brands (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  name TEXT NOT NULL,
  slogan TEXT,
  description TEXT,
  voice_config JSONB NOT NULL, -- 品牌声音配置
  audience_config JSONB, -- 受众画像
  content_rules JSONB, -- 内容规则
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### contents（内容表）
```sql
CREATE TABLE contents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  brand_id UUID REFERENCES brands(id),
  title TEXT,
  content TEXT, -- Markdown/JSON
  content_type TEXT, -- article, note, script
  status TEXT DEFAULT 'draft', -- draft, scheduled, published
  platform_versions JSONB, -- 各平台版本
  scheduled_at TIMESTAMP,
  published_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB
);
```

#### platform_posts（平台发布表）
```sql
CREATE TABLE platform_posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_id UUID REFERENCES contents(id),
  platform TEXT NOT NULL, -- wechat, xiaohongshu, douyin, bilibili, weibo
  platform_content_id TEXT, -- 平台侧的内容 ID
  title TEXT,
  content TEXT,
  status TEXT, -- pending, published, failed
  published_at TIMESTAMP,
  url TEXT,
  metrics JSONB, -- 数据快照
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### comments（评论表）
```sql
CREATE TABLE comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  platform_post_id UUID REFERENCES platform_posts(id),
  platform_comment_id TEXT,
  user_id UUID REFERENCES users(id),
  content TEXT NOT NULL,
  author TEXT, -- 评论者
  author_platform_id TEXT,
  classification TEXT, -- question, praise, criticism, spam
  priority INTEGER DEFAULT 0,
  status TEXT DEFAULT 'pending', -- pending, replied, ignored
  ai_reply TEXT, -- AI 生成的回复
  user_reply TEXT, -- 用户确认的回复
  replied_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB
);
```

#### platform_metrics（平台数据表）
```sql
CREATE TABLE platform_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  platform_post_id UUID REFERENCES platform_posts(id),
  platform TEXT NOT NULL,
  date DATE NOT NULL,
  metrics JSONB NOT NULL,
  -- 常见指标：views, likes, comments, shares, collects, completions
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(platform_post_id, date)
);
```

#### media_assets（素材表）
```sql
CREATE TABLE media_assets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  brand_id UUID REFERENCES brands(id),
  type TEXT NOT NULL, -- image, video, text, template
  url TEXT NOT NULL,
  thumbnail_url TEXT,
  title TEXT,
  description TEXT,
  tags TEXT[], -- 标签数组
  ai_tags TEXT[], -- AI 自动生成的标签
  metadata JSONB, -- 尺寸、格式、时长等
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### templates（模板表）
```sql
CREATE TABLE templates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  brand_id UUID REFERENCES brands(id),
  name TEXT NOT NULL,
  description TEXT,
  type TEXT NOT NULL, -- title, structure, platform
  content TEXT NOT NULL, -- 模板内容
  variables JSONB, -- 变量定义
  tags TEXT[],
  is_public BOOLEAN DEFAULT false,
  usage_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### knowledge_base（知识库表）
```sql
CREATE TABLE knowledge_base (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  brand_id UUID REFERENCES brands(id),
  category TEXT, -- faq, product, story, data
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  tags TEXT[],
  vector_embedding vector(1536), -- 向量嵌入
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### insights（洞察表）
```sql
CREATE TABLE insights (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  brand_id UUID REFERENCES brands(id),
  type TEXT, -- pattern, suggestion, alert
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  priority TEXT, -- low, medium, high
  data JSONB, -- 支撑数据
  is_read BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### scheduled_jobs（定时任务表）
```sql
CREATE TABLE scheduled_jobs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  type TEXT NOT NULL, -- publish, sync, analytics
  payload JSONB NOT NULL,
  scheduled_at TIMESTAMP NOT NULL,
  status TEXT DEFAULT 'pending', -- pending, running, completed, failed
  executed_at TIMESTAMP,
  result JSONB,
  error TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5.2 配置文件格式

#### brand.yml（品牌配置）
```yaml
# 品牌配置文件
name: "职场充电宝"
slogan: "每天充电，快速成长"

voice:
  tone: "friendly, encouraging, practical"
  personality: "像一个靠谱的前辈，温暖但不鸡汤"
  language: "简单易懂，避免术语，多用比喻"

  do:
    - 用"我们"拉近与读者的距离
    - 多给具体的行动建议
    - 用真实的职场案例

  dont:
    - 不要说教
    - 不要用"必须"、"应该"等强势词汇
    - 不要制造焦虑

audience:
  age: "22-35岁"
  role: "职场新人到中层管理者"
  painPoints:
    - "想成长但不知道方法"
    - "职场人际关系复杂"
    - "工作与生活不平衡"

contentRules:
  titleStyle: "数字+痛点/利益点，例如：3个方法让你..."
  structure: "故事开场 → 3个要点 → 总结行动"
  cta: "评论区互动引导，而非生硬的'关注我'"

platforms:
  wechat:
    enabled: true
    minLength: 1000
    maxLength: 5000
  xiaohongshu:
    enabled: true
    minLength: 200
    maxLength: 1000
    useEmoji: true
```

---

## 6. API 设计

### 6.1 核心内部 API

#### 6.1.1 Content API（内容）

```typescript
interface ContentService {
  // 创建内容
  createContent(
    input: CreateContentInput
  ): Promise<Content>;

  // 获取内容
  getContent(contentId: string): Promise<Content>;

  // 列出内容
  listContents(
    options?: ListContentsOptions
  ): Promise<Content[]>;

  // 更新内容
  updateContent(
    contentId: string,
    input: UpdateContentInput
  ): Promise<Content>;

  // AI 辅助写作
  aiWrite(
    contentId: string,
    prompt: string,
    options?: AiWriteOptions
  ): Promise<AsyncIterable<string>>;

  // 生成多平台版本
  generatePlatformVersions(
    contentId: string,
    platforms: string[]
  ): Promise<PlatformVersion[]>;

  // 安排发布
  schedulePublish(
    contentId: string,
    platform: string,
    scheduledAt: Date
  ): Promise<ScheduledPublish>;

  // 立即发布
  publishNow(
    contentId: string,
    platforms: string[]
  ): Promise<PublishResult[]>;
}
```

#### 6.1.2 Brand API（品牌）

```typescript
interface BrandService {
  // 创建品牌
  createBrand(
    input: CreateBrandInput
  ): Promise<Brand>;

  // 获取品牌
  getBrand(brandId: string): Promise<Brand>;

  // 更新品牌
  updateBrand(
    brandId: string,
    input: UpdateBrandInput
  ): Promise<Brand>;

  // 导入历史内容
  importHistoricalContent(
    brandId: string,
    contents: HistoricalContent[]
  ): Promise<ImportResult>;

  // 分析品牌调性
  analyzeBrandVoice(
    brandId: string
  ): Promise<BrandVoiceAnalysis>;

  // 品牌一致性检查
  checkBrandConsistency(
    brandId: string,
    content: string
  ): Promise<ConsistencyCheckResult>;
}
```

#### 6.1.3 Platform API（平台集成）

```typescript
interface PlatformService {
  // 连接平台
  connectPlatform(
    platform: string,
    credentials: PlatformCredentials
  ): Promise<PlatformConnection>;

  // 断开平台
  disconnectPlatform(
    platform: string
  ): Promise<void>;

  // 获取连接状态
  getConnectionStatus(
    platform: string
  ): Promise<ConnectionStatus>;

  // 同步数据
  syncData(
    platform: string,
    options?: SyncOptions
  ): Promise<SyncResult>;

  // 发布内容
  publishContent(
    platform: string,
    content: PlatformContent
  ): Promise<PublishResult>;

  // 获取评论
  fetchComments(
    platform: string,
    options?: FetchOptions
  ): Promise<Comment[]>;

  // 回复评论
  replyComment(
    platform: string,
    commentId: string,
    reply: string
  ): Promise<void>;
}
```

#### 6.1.4 Engagement API（互动）

```typescript
interface EngagementService {
  // 获取待处理评论
  getPendingComments(
    options?: PendingOptions
  ): Promise<Comment[]>;

  // 分类评论
  classifyComment(
    commentId: string
  ): Promise<CommentClassification>;

  // 生成回复
  generateReply(
    commentId: string,
    options?: ReplyOptions
  ): Promise<ReplySuggestion[]>;

  // 确认回复
  confirmReply(
    commentId: string,
    reply: string
  ): Promise<void>;

  // 批量感谢
  batchThank(
    commentIds: string[]
  ): Promise<void>;

  // 获取互动洞察
  getEngagementInsights(
    options?: InsightsOptions
  ): Promise<EngagementInsights>;
}
```

#### 6.1.5 Analytics API（分析）

```typescript
interface AnalyticsService {
  // 获取今日简报
  getDailyBrief(
    date?: Date
  ): Promise<DailyBrief>;

  // 获取内容表现
  getContentPerformance(
    options?: PerformanceOptions
  ): Promise<ContentPerformance[]>;

  // 获取趋势数据
  getTrends(
    options?: TrendOptions
  ): Promise<TrendData>;

  // 生成洞察
  generateInsights(
    options?: InsightOptions
  ): Promise<Insight[]>;

  // 导出报告
  exportReport(
    type: string,
    options?: ExportOptions
  ): Promise<ExportResult>;

  // 获取平台对比
  getPlatformComparison(
    options?: ComparisonOptions
  ): Promise<PlatformComparison>;
}
```

#### 6.1.6 Media API（素材）

```typescript
interface MediaService {
  // 上传素材
  uploadMedia(
    file: File,
    options?: UploadOptions
  ): Promise<MediaAsset>;

  // 获取素材
  getMedia(mediaId: string): Promise<MediaAsset>;

  // 搜索素材
  searchMedia(
    query: string,
    options?: SearchOptions
  ): Promise<MediaAsset[]>;

  // AI 打标签
  autoTagMedia(
    mediaId: string
  ): Promise<string[]>;

  // 智能配图
  suggestImages(
    content: string,
    options?: SuggestOptions
  ): Promise<MediaAsset[]>;

  // 生成封面
  generateCover(
    title: string,
    platform: string,
    options?: CoverOptions
  ): Promise<GeneratedCover>;
}
```

### 6.2 提示词模板

```typescript
const PROMPTS = {
  brandVoiceAnalysis: `你是一位品牌分析专家。
请分析以下历史内容，提取品牌调性和风格特征。

历史内容示例：
{{historicalContents}}

请分析：
1. 品牌声音（语气、用词、句式）
2. 目标受众特征
3. 内容结构偏好
4. 可以复用的模板

输出格式：JSON`,

  contentGeneration: `你是一位专业的内容创作者，也是{{brandName}}的品牌代言人。

品牌档案：
{{brandProfile}}

历史内容风格参考：
{{styleExamples}}

请根据以下要求创作内容：
主题：{{topic}}
平台：{{platform}}
长度：{{length}}

要求：
1. 严格符合品牌调性
2. 参考历史内容风格
3. 适合{{platform}}平台
4. 有吸引力的标题
5. 清晰的结构
6. 引导互动的结尾`,

  platformAdaptation: `你是一位多平台内容专家。
请将以下内容适配到{{targetPlatform}}平台。

原始内容（{{sourcePlatform}}）：
{{sourceContent}}

目标平台特点：
{{platformCharacteristics}}

请生成：
1. 适合{{targetPlatform}}的标题
2. 适配后的内容
3. 合适的话题标签（如适用）

要求：
- 保留核心信息
- 调整长度和风格
- 符合目标平台特性`,

  commentReply: `你是{{brandName}}的社区运营。

品牌档案：
{{brandProfile}}

用户评论：
{{comment}}

评论分类：{{classification}}

请生成3个回复选项：
1. 亲切版 - 温暖友好
2. 简洁版 - 简短直接
3. 互动版 - 引导更多对话

要求：
- 符合品牌调性
- 真诚自然，不生硬
- {{additionalInstructions}}`,

  insightsGeneration: `你是一位数据分析师和内容策略专家。
请分析以下数据，生成有价值的洞察和建议。

数据概览：
{{dataSummary}}

内容表现：
{{contentPerformance}}

趋势数据：
{{trendData}}

请提供：
1. 3-5个关键发现（有数据支撑）
2. 3-5个 actionable 建议
3. 1-2个需要关注的风险

输出格式：Markdown，清晰的标题和要点`
};
```

---

## 7. 用户故事与验收标准

### 史诗 1：品牌理解

#### US 1.1：建立品牌档案
**作为**内容运营，**我希望**通过引导式向导建立品牌档案，**这样**Claude 就能理解我们的品牌。

**验收标准**：
- [ ] 有 5 步以内的引导式向导
- [ ] 可以设置品牌名称、slogan、价值观
- [ ] 可以选择品牌声音（预设选项 + 自定义）
- [ ] 可以定义目标受众画像
- [ ] 10 分钟内可以完成配置

**优先级**：P0
**估点**：5
**依赖**：无

---

#### US 1.2：导入历史内容
**作为**内容运营，**我希望**导入历史内容，**这样**Claude 就能学习我们的风格。

**验收标准**：
- [ ] 支持导入公众号文章（至少 3 个平台）
- [ ] 可以批量导入（100 篇以上）
- [ ] 显示导入进度
- [ ] 导入失败有重试选项
- [ ] 能看到导入的内容列表

**优先级**：P0
**估点**：8
**依赖**：US 1.1

---

#### US 1.3：品牌一致性检查
**作为**内容运营，**我希望**Claude 检查内容是否符合品牌，**这样**我们的内容风格就一致了。

**验收标准**：
- [ ] 实时提示"这可能不符合品牌调性"
- [ ] 指出具体哪里不符合
- [ ] 提供修改建议
- [ ] 可以调整"品牌严格度"
- [ ] 可以选择"忽略这次"

**优先级**：P1
**估点**：5
**依赖**：US 1.1, US 1.2

---

### 史诗 2：多平台内容

#### US 2.1：创作内容
**作为**内容运营，**我希望**在 Claude 里写内容，**这样**我就能得到 AI 辅助。

**验收标准**：
- [ ] 支持 Markdown 编辑
- [ ] 有 AI 辅助工具栏（续写、扩写、缩写、改写）
- [ ] 有智能提示（"这里可以加个案例"）
- [ ] 自动保存（防止丢失）
- [ ] 可以插入素材库的内容

**优先级**：P0
**估点**：8
**依赖**：无

---

#### US 2.2：生成多平台版本
**作为**多平台运营，**我希望**一键生成所有平台版本，**这样**我就不用反复改写了。

**验收标准**：
- [ ] 可以选择要生成的平台
- [ ] 10 秒内生成 5 个平台版本
- [ ] 每个版本符合该平台风格
- [ ] 可以单独编辑每个版本
- [ ] 可以对比原始内容

**优先级**：P0
**估点**：13
**依赖**：US 2.1

---

#### US 2.3：定时发布
**作为**内容运营，**我希望**安排定时发布，**这样**我就不用守着发布时间了。

**验收标准**：
- [ ] 有内容日历视图（周/月）
- [ ] 可以拖拽安排发布时间
- [ ] 有平台最佳发布时间建议
- [ ] 定时发布准时执行
- [ ] 发布失败有提醒和重试

**优先级**：P0
**估点**：5
**依赖**：US 2.2

---

### 史诗 3：互动助手

#### US 3.1：查看所有评论
**作为**内容运营，**我希望**在一个地方看所有平台的评论，**这样**我就不用一个个平台去看了。

**验收标准**：
- [ ] 聚合 5 个主要平台的评论
- [ ] 评论按时间/热度排序
- [ ] 可以按平台筛选
- [ ] 可以按状态筛选（待处理/已回复）
- [ ] 5 分钟内同步新评论

**优先级**：P0
**估点**：8
**依赖**：无

---

#### US 3.2：AI 生成回复
**作为**内容运营，**我希望**AI 帮我写回复，**这样**我就能更快地互动了。

**验收标准**：
- [ ] AI 能生成 3 个回复选项
- [ ] 回复符合品牌调性
- [ ] 可以一键确认发布
- [ ] 可以修改后再发布
- [ ] 回复采用率 >75%

**优先级**：P0
**估点**：8
**依赖**：US 3.1, US 1.1

---

#### US 3.3：批量处理
**作为**内容运营，**我希望**批量处理评论，**这样**我就能节省时间了。

**验收标准**：
- [ ] 可以"一键感谢所有赞美"
- [ ] 可以批量点赞高价值评论
- [ ] 可以选择"处理所有已审核的"
- [ ] 有撤销选项
- [ ] 能看到处理统计

**优先级**：P1
**估点**：5
**依赖**：US 3.2

---

### 史诗 4：数据看板

#### US 4.1：查看今日简报
**作为**内容运营，**我希望**每天早上看今日简报，**这样**我就能快速了解情况。

**验收标准**：
- [ ] 今日简报 3 秒内加载
- [ ] 展示关键数据（阅读、互动、新粉）
- [ ] 显示最佳表现内容
- [ ] 有智能建议
- [ ] 显示需要关注的事项

**优先级**：P0
**估点**：5
**依赖**：无

---

#### US 4.2：查看详细数据
**作为**内容运营，**我希望**看详细的数据和趋势，**这样**我就能分析表现了。

**验收标准**：
- [ ] 有内容表现表格（可排序、筛选）
- [ ] 有趋势图（日/周/月）
- [ ] 可以对比不同平台
- [ ] 可以对比不同内容类型
- [ ] 数据准确（>99%）

**优先级**：P0
**估点**：8
**依赖**：US 4.1

---

#### US 4.3：获取智能洞察
**作为**内容运营，**我希望**AI 给我洞察和建议，**这样**我就能做得更好了。

**验收标准**：
- [ ] AI 能发现 3-5 个关键规律
- [ ] 每个规律有数据支撑
- [ ] 有 3-5 个 actionable 建议
- [ ] 建议可以标记"已采纳"
- [ ] 用户觉得"有启发"（>80%）

**优先级**：P1
**估点**：8
**依赖**：US 4.2

---

#### US 4.4：导出周报
**作为**内容运营，**我希望**一键导出周报，**这样**我就能给老板看了。

**验收标准**：
- [ ] 有预设的周报模板
- [ ] 可以导出 PDF/Excel/PPT
- [ ] 可以自定义周报内容
- [ ] 导出时间 < 10 秒
- [ ] 格式美观专业

**优先级**：P1
**估点**：5
**依赖**：US 4.2

---

### 史诗 5：素材库

#### US 5.1：上传和管理素材
**作为**内容运营，**我希望**管理我的素材，**这样**我就能快速找到需要的。

**验收标准**：
- [ ] 可以上传图片、视频、文案
- [ ] 可以创建文件夹/相册
- [ ] 可以给素材打标签
- [ ] 可以编辑素材信息
- [ ] 可以删除素材

**优先级**：P0
**估点**：5
**依赖**：无

---

#### US 5.2：搜索素材
**作为**内容运营，**我希望**快速搜索素材，**这样**我就不用翻半天了。

**验收标准**：
- [ ] 可以用关键词搜索
- [ ] 可以用自然语言搜索（"找一张职场开会的图片"）
- [ ] 可以按标签筛选
- [ ] 可以按类型筛选
- [ ] 搜索结果 1 秒内返回

**优先级**：P0
**估点**：8
**依赖**：US 5.1

---

#### US 5.3：使用标题模板
**作为**内容运营，**我希望**用标题模板，**这样**我就能写出更好的标题了。

**验收标准**：
- [ ] 有 100+ 预设标题模板
- [ ] 模板分类清晰
- [ ] 可以预览模板效果
- [ ] 可以保存自己的模板
- [ ] 用户觉得"模板有用"（>80%）

**优先级**：P1
**估点**：5
**依赖**：无

---

## 8. 冲刺计划

### Sprint 1：基础框架 + 品牌理解（2 周）

**目标**：建立产品基础架构，完成品牌理解核心功能

**用户故事**：
- US 1.1：建立品牌档案（5 点）
- US 1.2：导入历史内容（8 点）

**技术任务**：
- [ ] 搭建 monorepo 项目结构
- [ ] 配置 TypeScript、ESLint、Prettier
- [ ] 设计并实现 PostgreSQL 数据模型
- [ ] 搭建 Next.js Web 应用基础
- [ ] 集成 Anthropic API 客户端
- [ ] 实现品牌档案配置界面
- [ ] 实现历史内容导入功能
- [ ] 提示词工程（品牌分析）

**验收**：
- [ ] 用户可以完成品牌档案配置
- [ ] 可以导入历史公众号文章
- [ ] 基础 Web 界面可用
- [ ] AI 品牌分析功能工作

---

### Sprint 2：内容创作 + 多平台适配（3 周）

**目标**：实现内容创作和多平台适配核心功能

**用户故事**：
- US 2.1：创作内容（8 点）
- US 2.2：生成多平台版本（13 点）

**技术任务**：
- [ ] 实现富文本编辑器（Markdown）
- [ ] 实现 AI 辅助写作工具栏
- [ ] 实现平台适配引擎
- [ ] 预设 5 个平台模板
- [ ] 实现内容版本管理
- [ ] 提示词工程（内容生成、平台适配）
- 多窗口布局

**验收**：
- [ ] 可以在编辑器中写内容
- [ ] AI 辅助写作功能可用
- [ ] 可以一键生成 5 个平台版本
- [ ] 每个平台版本符合该平台风格

---

### Sprint 3：平台集成 + 定时发布（2 周）

**目标**：实现平台集成和内容发布功能

**用户故事**：
- US 2.3：定时发布（5 点）
- US 3.1：查看所有评论（8 点）

**技术任务**：
- [ ] 实现公众号 API 集成
- [ ] 实现小红书 API 集成
- [ ] 实现抖音 API 集成
- [ ] 实现内容日历 UI
- [ ] 实现定时任务调度器（BullMQ）
- [ ] 实现评论聚合功能
- [ ] 发布流程测试

**验收**：
- [ ] 可以连接 3 个主要平台
- [ ] 内容日历可以拖拽安排发布
- [ ] 定时发布功能正常工作
- [ ] 所有平台的评论聚合到一个地方

---

### Sprint 4：互动助手 + 数据看板（3 周）

**目标**：实现 AI 互动助手和数据看板功能

**用户故事**：
- US 3.2：AI 生成回复（8 点）
- US 3.3：批量处理（5 点）
- US 4.1：查看今日简报（5 点）
- US 4.2：查看详细数据（8 点）

**技术任务**：
- [ ] 实现评论分类算法
- [ ] 实现 AI 回复生成
- [ ] 实现批量处理功能
- [ ] 实现今日简报 UI
- [ ] 实现数据看板（图表、表格）
- [ ] 实现数据聚合和 ETL
- [ ] 提示词工程（回复生成）

**验收**：
- [ ] AI 能生成评论回复
- [ ] 可以批量处理评论
- [ ] 今日简报清晰展示关键数据
- [ ] 详细数据看板可用

---

### Sprint 5：素材库 + 洞察 + 移动端（3 周）

**目标**：实现素材库、智能洞察和移动端基础

**用户故事**：
- US 4.3：获取智能洞察（8 点）
- US 4.4：导出周报（5 点）
- US 5.1：上传和管理素材（5 点）
- US 5.2：搜索素材（8 点）
- US 5.3：使用标题模板（5 点）

**技术任务**：
- [ ] 实现素材上传和管理
- [ ] 实现 AI 自动标签
- [ ] 实现智能搜索（自然语言）
- [ ] 实现标题模板库
- [ ] 实现智能洞察生成
- [ ] 实现报表导出
- [ ] 搭建 React Native 移动端基础
- [ ] 提示词工程（洞察生成）
- UX 优化、性能优化
- 错误边界和崩溃恢复
- Analytics 集成
- 打包和发布准备

**验收**：
- [ ] 素材库功能完整
- [ ] 可以用自然语言搜索素材
- [ ] 智能洞察能发现有价值的规律
- [ ] 周报可以一键导出
- [ ] 移动端核心功能可用
- 所有核心功能完整
- 无严重 bug
- 准备 Beta 发布

---

## 9. 测试策略

### 9.1 测试金字塔

```
        /\          E2E 测试（5%）
       /--\         集成测试（15%）
      /----\        单元测试（80%）
     /--------\
```

### 9.2 单元测试

**覆盖范围**：
- 所有核心服务
- 工具函数
- 数据模型验证
- 提示词模板验证
- 平台适配逻辑

**框架**：Jest + Testing Library

**目标覆盖率**：> 80%

**示例测试**：
```typescript
describe('BrandVoiceService', () => {
  describe('analyzeBrandVoice', () => {
    it('should analyze brand voice from historical content', async () => {
      const service = new BrandVoiceService();
      const analysis = await service.analyzeBrandVoice([
        { title: '3个方法...', content: '...' },
        { title: '别再...', content: '...' }
      ]);

      expect(analysis.tone).toBeDefined();
      expect(analysis.wordPatterns).toHaveLength(5);
    });
  });
});

describe('PlatformAdapter', () => {
  describe('adaptToXiaohongshu', () => {
    it('should adapt content to Xiaohongshu style', async () => {
      const adapter = new PlatformAdapter();
      const result = await adapter.adapt(
        '这是一篇很长的文章...',
        'xiaohongshu'
      );

      expect(result.length).toBeLessThan(1000);
      expect(result.includes('✨')).toBe(true);
    });
  });
});
```

### 9.3 AI 输出测试（特别重要）

**测试策略**：
- **Golden Master 测试**：保存已知好的输出作为基准
- **A/B 测试**：提示词变更时做对比
- **人工审查**：关键路径输出需要人工审查
- **评分模型**：自动评分 + 人工评分

**评分维度**：
- 相关性：内容是否相关
- 正确性：事实是否准确
- 品牌一致性：是否符合品牌调性
- 有用性：对用户是否有帮助
- 安全性：是否有敏感/违规内容

**示例测试集**：
```typescript
const AI_TEST_CASES = [
  {
    name: '职场内容生成',
    input: '写一篇关于职场沟通的公众号文章',
    brand: '职场充电宝',
    expectedChecks: [
      '有明确的标题',
      '有3个要点',
      '符合品牌调性',
      '有互动结尾'
    ]
  },
  {
    name: '小红书适配',
    input: '将这篇长文改成小红书版本',
    platform: 'xiaohongshu',
    expectedChecks: [
      '长度合适（300-800字）',
      '有emoji',
      '分段清晰',
      '有话题标签'
    ]
  },
  {
    name: '评论回复',
    input: '用户评论："这篇太实用了！能不能出一期职场沟通？"',
    type: 'praise + question',
    expectedChecks: [
      '感谢用户',
      '回答问题',
      '符合品牌调性',
      '引导进一步互动'
    ]
  }
];
```

### 9.4 集成测试

**覆盖范围**：
- 服务间交互
- 数据库操作
- Anthropic API 集成（使用 mock）
- 平台 API 集成（使用 mock）

### 9.5 E2E 测试

**覆盖范围**：
- 核心用户流程
- 跨平台一致性

**框架**：Playwright

**关键流程**：
1. 品牌档案配置 → 导入历史内容 → 写内容 → 生成多平台版本 → 定时发布
2. 查看今日简报 → 查看评论 → AI 生成回复 → 确认发布
3. 上传素材 → 搜索素材 → 插入到内容中

---

## 10. 监控与指标

### 10.1 产品指标

| 指标 | 目标 | 警报阈值 |
|------|------|---------|
| 试用→付费转化 | >12% | <8% |
| 周活跃率 | >55% | <40% |
| 月留存率 | >65% | <45% |
| NPS | >45 | <30 |
| 工作流完成率 | >75% | <60% |
| 内容采用率 | >80% | <60% |
| 回复采用率 | >75% | <60% |

### 10.2 技术指标

| 指标 | 目标 | 警报阈值 |
|------|------|---------|
| API 错误率 | <5% | >10% |
| API p95 响应时间 | <3s | >5s |
| AI 生成时间 | <10s | >15s |
| 内容发布成功率 | >99% | <95% |
| 数据同步延迟 | <1h | >2h |
| AI 成本/收入 | <35% | >45% |

### 10.3 护栏指标

**用户满意度护栏**：
- [ ] 内容采用率 <60% → 警报
- [ ] 回复采用率 <60% → 警报
- [ ] NPS <30 → 警报

**性能护栏**：
- [ ] AI 生成时间 >15s → 警报
- [ ] 错误率 >10% → 警报

**成本护栏**：
- [ ] AI 成本/收入 >45% → 警报

### 10.4 每周指标回顾模板

| 指标 | 上周 | 本周 | 变化 | 评论 |
|------|------|------|------|------|
| 周活跃用户 | | | | |
| 月留存率 | | | | |
| 试用→付费转化 | | | | |
| MRR | | | | |
| NPS | | | | |
| 内容采用率 | | | | |
| AI 生成时间 | | | | |
| AI 成本/收入 | | | | |

---

## 11. 风险与依赖

### 11.1 风险登记册

| 风险 | 影响 | 可能性 | 优先级 | 缓解措施 | 负责人 |
|------|------|--------|--------|---------|--------|
| 平台 API 限制/变更 | 🔴 严重 | 🟡 中 | P0 | 多个平台支持，降级方案，平台无关的数据模型 | 后端 |
| AI 内容质量不稳定 | 🔴 严重 | 🟡 中 | P0 | 提示词工程，人工审核流程，用户反馈机制 | PM/AI |
| 用户对 AI 内容的信任 | 🟡 中 | 🟢 高 | P1 | 透明的 AI 标识，用户完全控制权，可编辑 | 设计/UX |
| 内容版权问题 | 🟡 中 | 🟡 中 | P1 | 原创声明，用户最终负责，法律条款 | 法务 |
| 竞品快速跟进 | 🟡 中 | 🟢 高 | P2 | 快速迭代，建立用户社区，品牌理解差异化 | 全团队 |

### 11.2 依赖项

| 依赖 | 类型 | 重要性 | 预计时间 | 备注 |
|------|------|--------|---------|------|
| Anthropic Claude API 访问 | 外部 | 🔴 关键 | Sprint 1 前 | 已确认 |
| 公众号 API 访问 | 外部 | 🟡 重要 | Sprint 3 前 | 待申请 |
| 小红书 API 访问 | 外部 | 🟡 重要 | Sprint 3 前 | 待申请 |
| 抖音 API 访问 | 外部 | 🟡 重要 | Sprint 3 前 | 待申请 |
| 云基础设施（AWS/GCP） | 外部 | 🟡 重要 | Sprint 2 前 | 可选 |

### 11.3 假设清单

| 假设 | 验证方法 | 状态 |
|------|---------|------|
| 内容运营愿意为多平台工具支付 $25/月 | 用户访谈、定价测试 | 待验证 |
| "品牌理解 + 多步骤工作流"是关键差异化 | 竞品对比测试 | 待验证 |
| 运营可以接受 AI 辅助，自己做最终决策 | 用户测试 | 待验证 |
| 30 分钟内体验"啊哈！"时刻 | onboarding funnel 分析 | 待验证 |

---

## 附录

### A. 平台特性对比表

| 平台 | 内容形式 | 理想长度 | 发布频率 | 互动特点 |
|------|---------|---------|---------|---------|
| **公众号** | 长图文 | 1500-3000 字 | 周更 2-3 次 | 在看、分享、收藏 |
| **小红书** | 笔记 | 300-800 字 | 日更 | 点赞、收藏、评论 |
| **抖音** | 短视频 | 15-60 秒 | 日更 | 完播率、点赞、评论 |
| **B站** | 中视频 | 5-15 分钟 | 周更 1-2 次 | 弹幕、投币、收藏 |
| **微博** | 短内容 | 140-300 字 | 日更多次 | 转发、评论、点赞 |
| **知乎** | 问答/专栏 | 1000-2000 字 | 周更 1-2 次 | 专业、可信、长回答 |

### B. 术语表

| 术语 | 定义 |
|------|------|
| PLG | Product-Led Growth，产品主导增长 |
| PMF | Product-Market Fit，产品市场匹配 |
| NPS | Net Promoter Score，净推荐值 |
| CAC | Customer Acquisition Cost，用户获取成本 |
| LTV | Lifetime Value，用户生命周期价值 |
| MVP | Minimum Viable Product，最小可行产品 |
| Brand Voice | 品牌声音，品牌的语言风格 |
| CT A | Call to Action，行动号召 |
| 完播率 | 视频播放完成的比例 |

### C. 变更历史

| 版本 | 日期 | 变更 | 作者 |
|------|------|------|------|
| 1.0 | 2026-03-16 | 初始版本，从 Claude Code 扩展而来 | AI 产品团队 |

---

**文档结束**

如有疑问，请联系产品团队。
