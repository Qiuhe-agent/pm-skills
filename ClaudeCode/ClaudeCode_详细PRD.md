# Claude Code - 产品需求文档 (PRD)

**面向**：开发团队
**版本**：v1.0 (MVP)
**日期**：2026-03-16
**状态**：开发就绪

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
> **"让每一位开发者都拥有一位 24/7 的智能编程伙伴，释放人类的创造潜能。"**

### 1.2 核心定位
Claude Code 不是简单的代码补全工具，而是**深度 AI 编程伙伴**：
- 理解整个代码库，而非单个文件
- 执行多步骤任务，而非单步操作
- 与现有工具集成，而非替代它们
- 人类始终拥有最终控制权

### 1.3 MVP 目标
- 验证核心价值：深度理解 + 多步骤自动化
- 建立早期用户反馈循环
- 验证产品主导增长（PLG）策略
- 实现产品市场匹配（PMF）

### 1.4 成功指标（MVP）

| 指标 | 目标 | 测量方式 |
|------|------|---------|
| 试用→付费转化率 | >15% | 计费系统 |
| 周活跃率 | >60% | 产品分析 |
| 月留存率 | >70% | 产品分析 |
| NPS | >40 | 用户调查 |
| 每周节省时间（用户报告） | >4 小时 | 用户调查 |
| 任务完成率 | >80% | 产品分析 |
| 代码接受率 | >70% | 产品分析 |

---

## 2. 目标用户与痛点

### 2.1 典型用户画像：Alex Chen

| 属性 | 描述 |
|------|------|
| **年龄** | 28 岁 |
| **角色** | 全栈开发者 |
| **经验** | 4 年 |
| **公司** | 20 人 SaaS 初创公司 |
| **技术栈** | React、Node.js、VS Code |
| **每日编码** | 6-8 小时 |
| **工具支出** | 已为多个开发者工具付费 |

### 2.2 核心痛点（按优先级）

| 痛点 | 量化 | 现有解决方案 | 我们的方案 |
|------|------|-------------|-----------|
| **重复性任务耗时** | 25-35% 工作时间 | 手动、脚本 | 多步骤自动化 |
| **上下文切换成本高** | 每次 15-30 分钟 | 无 | 深度代码库理解 |
| **现有 AI 工具理解不够** | 需要大量纠正 | Copilot/Cursor | 理解项目约定 |
| **团队知识难以传承** | 新人上手需 2-3 个月 | 文档、mentoring | 技能系统 |

---

## 3. 核心功能详细规格

### 3.1 F1：深度代码库理解

#### 3.1.1 功能描述
Claude Code 能够索引、理解和记忆整个代码库的结构、依赖、约定和历史。

#### 3.1.2 用户故事
> 作为开发者，我希望 Claude 理解我的整个项目，这样它的建议才符合我们的约定和架构。

#### 3.1.3 功能需求

**3.1.3.1 代码库索引**
- 自动检测项目根目录（通过 .git、package.json 等标记）
- 可配置的排除规则（.gitignore + 额外排除）
- 增量索引：只重新索引变更的文件
- 索引进度显示（百分比 + 已处理文件数）
- 索引状态持久化，重启后不需要重新索引

**3.1.3.2 语义分析**
- 解析抽象语法树（AST）
- 识别符号定义和引用
- 构建调用图和依赖图
- 识别代码模式和惯用写法
- 提取文档注释和类型信息

**3.1.3.3 约定学习**
- 观察现有代码，推断命名约定
- 识别代码风格（缩进、引号、分号等）
- 学习架构模式和设计决策
- 可以显式定义约定（通过配置文件）

**3.1.3.4 上下文记忆**
- 记住对话历史（跨会话）
- 关联对话与代码位置
- 理解用户的隐含意图
- 支持"继续刚才的话题"

#### 3.1.4 非功能需求

| 指标 | 目标 | 备注 |
|------|------|------|
| 初始索引时间 | < 5 分钟 | 中型项目（10k 文件） |
| 增量更新时间 | < 30 秒 | 单文件变更 |
| 内存占用 | < 500MB | 空闲状态 |
| 索引存储大小 | < 100MB | 中型项目 |
| 索引格式 | 可迁移 | 版本更新时不需要重索引 |

#### 3.1.5 验收标准

- [ ] 打开新项目时自动开始索引，显示进度
- [ ] 索引完成后，Claude 能正确回答关于代码库架构的问题
- [ ] Claude 的建议符合团队已有的代码风格
- [ ] 修改文件后，增量索引在 30 秒内完成
- [ ] 重启应用后，索引状态保持，不需要重新索引
- [ ] 可以正确引用项目其他部分的代码

---

### 3.2 F2：多步骤任务自动化

#### 3.2.1 功能描述
用户用自然语言描述复杂任务，Claude 规划并执行多步骤工作流，每一步都可预览和确认。

#### 3.2.2 用户故事
> 作为开发者，我希望告诉 Claude"为 auth 模块写测试，运行它们，修复失败"，这样我就不用手动一步步做了。

#### 3.2.3 功能需求

**3.2.3.1 自然语言任务描述**
- 支持自由文本输入任务描述
- 提供常用任务模板（快捷短语）
- 支持多轮对话澄清任务细节
- 任务历史记录和重用

**3.2.3.2 任务分解和规划**
- 将复杂任务分解为可执行的步骤
- 显示任务计划（步骤列表）供用户确认
- 每个步骤包含：操作描述、预期影响、风险提示
- 支持用户修改计划（添加/删除/重排步骤）

**3.2.3.3 分步执行与确认**
- 逐个步骤执行
- 执行前显示预览（diff、命令输出等）
- 支持：确认、跳过、修改、取消
- 批量确认选项（"确认所有"）

**3.2.3.4 内置工作流模板**

| 模板 | 描述 | 步骤 |
|------|------|------|
| **测试生成** | 为指定模块生成测试 | 1. 分析代码 2. 生成测试 3. 预览 4. 确认 |
| **测试 + 修复** | 生成测试并修复失败 | 1. 生成测试 2. 运行 3. 分析失败 4. 修复 5. 重复 |
| **代码重构** | 安全地重构代码 | 1. 分析 2. 规划重构 3. 执行 4. 验证 |
| **Lint 修复** | 修复 lint 错误 | 1. 运行 lint 2. 分析 3. 修复 4. 确认 |
| **合并冲突** | 解决合并冲突 | 1. 分析冲突 2. 提出解决方案 3. 确认 |

**3.2.3.5 错误处理与恢复**
- 检测执行错误
- 提供错误分析和恢复选项
- 支持回滚到上一个安全点
- 完整的执行日志

**3.2.3.6 保存和重用工作流**
- 将当前任务保存为模板
- 给工作流命名、添加描述和标签
- 从库中快速选择已保存的工作流
- 支持参数化模板（占位符变量）
- 分享工作流给团队（导出/导入）

#### 3.2.4 非功能需求

| 指标 | 目标 |
|------|------|
| 任务规划时间 | < 10 秒 |
| 每步操作预览加载 | < 2 秒 |
| 任务执行可中断 | 随时可暂停/取消 |
| 状态保存 | 崩溃后可恢复未完成任务 |

#### 3.2.5 验收标准

- [ ] 用户可以说"为 auth.service.ts 写测试"，Claude 理解并执行
- [ ] 任务执行前显示清晰的计划，用户可以确认或修改
- [ ] 所有变更都有 diff 预览
- [ ] 用户可以成功完成"测试生成 → 运行 → 修复"完整工作流
- [ ] 可以保存一个工作流并在以后重用
- [ ] 执行出错时可以回滚到之前的状态

---

### 3.3 F3：技能（Skills）系统（基础版）

#### 3.3.1 功能描述
用户可以创建和使用"技能"——可复用的指令、知识和工作流。

#### 3.3.2 用户故事
> 作为团队技术主管，我希望定义团队的代码规范作为技能，这样 Claude 会自动遵守这些规范。

#### 3.3.3 功能需求

**3.3.3.1 技能定义语言**
- 使用简单的 YAML/Markdown 格式
- 支持的指令类型：
  - `rules`：规则和约束
  - `examples`：示例代码
  - `context`：上下文信息
  - `workflows`：工作流模板
- 示例格式：
```yaml
name: React 最佳实践
version: 1.0
description: 我们团队的 React 约定

rules:
  - 总是使用函数组件，不使用类组件
  - 使用 TypeScript，类型定义在 .d.ts 文件
  - 组件文件使用 PascalCase，工具函数使用 camelCase

examples:
  good: |
    // 好的写法
    const MyComponent = () => { ... }
  bad: |
    // 不好的写法
    class MyComponent extends React.Component { ... }
```

**3.3.3.2 内置技能库**
- 代码风格技能（Prettier/ESLint 风格）
- 框架特定技能（React、Vue、Angular）
- 语言特定技能（TypeScript、Python、Go）
- 最佳实践技能（安全、性能、可维护性）
- 每个技能都有：名称、描述、版本、作者、标签

**3.3.3.3 技能激活与配置**
- 技能浏览器：浏览和搜索技能库
- 一键激活/停用技能
- 可以同时激活多个技能（按优先级排序）
- 项目特定技能（.claude/skills 目录）
- 全局技能（用户级）

**3.3.3.4 技能市场（基础版）**
- 浏览公开技能
- 下载和安装技能
- 技能评分和评论（后续版本）
- 上传和分享技能（后续版本）

#### 3.3.4 非功能需求

| 指标 | 目标 |
|------|------|
| 技能加载时间 | < 1 秒 |
| 技能文件大小 | < 100KB |
| 技能验证 | 实时验证语法错误 |

#### 3.3.5 验收标准

- [ ] 用户可以创建一个简单的代码风格技能
- [ ] Claude 在生成代码时会遵守技能中的指令
- [ ] 用户可以从技能库浏览和安装内置技能
- [ ] 可以同时激活多个技能
- [ ] 项目特定技能只对当前项目生效

---

### 3.4 F4：跨平台支持（终端 + VS Code）

#### 3.4.1 功能描述
在终端和 VS Code 中提供一致的体验，用户可以在不同场景选择合适的工具。

#### 3.4.2 用户故事
> 作为开发者，我希望在终端快速做一些事，在 VS Code 做另一些，并且两个地方的 Claude 是一致的。

#### 3.4.3 功能需求

**3.4.3.1 终端版本（CLI）**

| 功能 | 描述 |
|------|------|
| 命令行接口 | `claude [command]` |
| 交互式模式 | `claude chat` 进入对话模式 |
| 任务执行 | `claude task "为 auth 写测试"` |
| Git 集成 | `claude review` 审查当前变更 |
| 配置管理 | `claude config set ...` |

**CLI 命令示例：**
```bash
# 启动交互式对话
claude

# 执行任务
claude task "为 src/auth 写测试"

# 审查代码
claude review

# 索引当前目录
claude index

# 配置
claude config set theme dark
```

**3.4.3.2 VS Code 扩展**

| 功能 | 描述 |
|------|------|
| 侧边栏对话 | 左侧/右侧面板中的对话界面 |
| 内联代码编辑 | 在编辑器中直接应用 AI 建议 |
| Diff 视图 | 专用的变更预览视图 |
| 命令面板集成 | `Ctrl+Shift+P` 搜索 Claude 命令 |
| 快捷键 | `Ctrl+L` 打开对话，`Ctrl+Enter` 确认 |
| 上下文菜单 | 右键选择"Ask Claude" |

**VS Code UI 布局：**
```
┌─────────────────────────────────────────────────┐
│  Explorer  │  Search  │  SCM  │  [CLAUDE]  │...│
├──────────────┬───────────────────────────────────┤
│              │  编辑器区域                        │
│  文件树      │                                   │
│              │                                   │
│              │                                   │
├──────────────┴───────────────────────────────────┤
│  Claude 侧边栏（可折叠）                          │
│  ┌─────────────────────────────────────────────┐ │
│  │  对话历史                      [新对话] [+] │ │
│  ├─────────────────────────────────────────────┤ │
│  │                                             │ │
│  │  Claude: 我理解了你的代码库，有什么我能帮   │ │
│  │          助的？                             │ │
│  │                                             │ │
│  │  你: "为 auth.service.ts 写测试"           │ │
│  │                                             │ │
│  ├─────────────────────────────────────────────┤ │
│  │  [消息输入框]                    [发送]     │ │
│  └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

**3.4.3.3 统一体验**

| 功能 | 描述 |
|------|------|
| 同步对话历史 | 跨平台同步对话 |
| 共享技能库 | 技能在所有平台可用 |
| 一致的 AI 能力 | 相同的模型和提示策略 |
| 配置同步 | 主题、偏好设置跨平台同步 |

#### 3.4.4 非功能需求

| 指标 | 目标 |
|------|------|
| VS Code 扩展安装 | < 1 分钟 |
| CLI 启动时间 | < 2 秒 |
| 同步延迟 | < 5 秒 |
| 离线可用 | 核心功能无网络也可用 |

#### 3.4.5 验收标准

- [ ] 用户可以在终端使用 `claude` 命令启动对话
- [ ] 用户可以在 VS Code 侧边栏中使用 Claude
- [ ] 对话历史在终端和 VS Code 间同步
- [ ] 在一个平台创建的技能在另一个平台也可用
- [ ] CLI 和 VS Code 中的功能体验一致

---

### 3.5 F5：安全和控制基础

#### 3.5.1 功能描述
确保用户可以安全地使用 Claude Code，保持完全的控制权和透明度。

#### 3.5.2 用户故事
> 作为开发者，我希望看到 Claude 要做的每一个变更，并能轻松回滚，这样我才放心。

#### 3.5.3 功能需求

**3.5.3.1 变更预览**
- 所有 AI 变更都有清晰的 diff 视图
- 统一的 diff 格式（类似 GitHub）
- 支持：行内 diff、并排 diff
- 高亮显示：添加（绿色）、删除（红色）、修改（黄色）
- 逐变更确认（可接受/拒绝单个变更）
- 批量确认选项

**Diff 视图示例：**
```diff
--- a/src/auth.service.ts
+++ b/src/auth.service.ts
@@ -15,6 +15,12 @@
 export class AuthService {
+  async validateToken(token: string): Promise<User> {
+    // 验证 JWT token
+    const payload = jwt.verify(token, SECRET);
+    return this.findUserById(payload.userId);
+  }
+
   async login(email: string, password: string): Promise<string> {
     const user = await this.findUserByEmail(email);
     if (!user) {
```

**3.5.3.2 回滚机制**
- 一键回滚到之前的状态
- 完整的操作历史（时间线视图）
- 支持选择性回滚（只回滚某些变更）
- 回滚后确认状态正确
- Git 集成：
  - 自动创建分支（可选）
  - 自动创建提交（带描述）
  - 回滚 = git reset / git revert

**3.5.3.3 隐私选项**
- 本地模式：代码不上传云端（需本地模型）
- 数据删除功能：一键删除所有云端数据
- 透明的数据使用政策：清晰说明什么数据被发送、为什么
- 可配置的数据共享：
  - 发送哪些文件
  - 不发送哪些文件（通过 .claudeignore）
  - 是否保存对话历史

**3.5.3.4 安全提示**
- 第一次使用时的安全向导
- 高风险操作前的确认提示
- 清晰的权限请求说明
- 定期安全提醒（可选）

#### 3.5.4 非功能需求

| 指标 | 目标 |
|------|------|
| 回滚操作 | < 5 秒 |
| Diff 视图加载 | < 2 秒 |
| 性能影响 | 不因安全功能明显下降 |

#### 3.5.5 验收标准

- [ ] 用户可以预览 AI 建议的所有变更
- [ ] 用户可以接受/拒绝单个变更
- [ ] 用户可以一键回滚所有变更
- [ ] Git 集成正常工作（自动创建提交）
- [ ] 用户可以配置哪些文件不发送
- [ ] 用户了解数据如何使用（清晰的说明）

---

## 4. 技术架构设计

### 4.1 系统概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                        用户界面层 (UI Layer)                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   终端 CLI    │  │  VS Code 扩展 │  │   Web UI     │          │
│  │  (Node.js)   │  │  (TypeScript) │  │  (React)     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      应用逻辑层 (App Logic Layer)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  对话管理器   │  │  任务规划器   │  │  技能系统     │          │
│  │              │  │              │  │              │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  变更预览     │  │  回滚引擎     │  │  同步服务     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    代码库理解层 (Code Understanding Layer)           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   索引器      │  │   语义分析    │  │  约定学习     │          │
│  │  (Tree-sitter)│  │  (AST 解析)   │  │  (模式匹配)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐                              │
│  │  符号解析器   │  │  依赖图构建   │                              │
│  └──────────────┘  └──────────────┘                              │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                        AI 模型层 (AI Model Layer)                    │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │           Claude 大语言模型（通过 Anthropic API）              │ │
│  │  - Claude 3.5 Sonnet（默认）                                   │ │
│  │  - Claude 3.5 Opus（高成本、高质量）                           │ │
│  │  - Claude 3.5 Haiku（低成本、低延迟）                           │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                        数据存储层 (Data Layer)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  本地 SQLite │  │  云端数据库   │  │  文件系统     │          │
│  │  (索引/配置)  │  │  (同步/历史)  │  │  (技能/项目)  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 关键技术决策

| 决策项 | 选择 | 理由 | 备选方案 |
|--------|------|------|---------|
| 前端语言 | TypeScript | 类型安全、生态成熟、跨平台 | JavaScript、Rust |
| UI 框架 | React | 组件化、VS Code 扩展支持 | Vue、Svelte |
| 代码索引 | Tree-sitter | 增量解析、多语言支持、快 | LSP、自定义解析器 |
| AI 模型 | Claude 3.5 Sonnet | 平衡质量和速度 | GPT-4、自研模型 |
| 数据存储 | SQLite + 云端同步 | 本地优先、隐私、可同步 | LevelDB、PostgreSQL |
| CLI 框架 | Commander.js | 成熟、易用 | oclif、yargs |

### 4.3 目录结构

```
claude-code/
├── packages/
│   ├── cli/                    # 终端 CLI
│   │   ├── src/
│   │   │   ├── commands/       # CLI 命令
│   │   │   ├── index.ts        # 入口
│   │   │   └── ...
│   │   └── package.json
│   │
│   ├── vscode/                 # VS Code 扩展
│   │   ├── src/
│   │   │   ├── extension.ts    # 扩展入口
│   │   │   ├── sidebar/        # 侧边栏 UI
│   │   │   ├── diff-view/      # Diff 视图
│   │   │   └── ...
│   │   └── package.json
│   │
│   ├── core/                   # 核心逻辑（共享）
│   │   ├── src/
│   │   │   ├── chat/           # 对话管理
│   │   │   ├── task/           # 任务规划和执行
│   │   │   ├── skills/         # 技能系统
│   │   │   ├── code-index/     # 代码索引
│   │   │   ├── git/            # Git 集成
│   │   │   ├── rollback/       # 回滚引擎
│   │   │   └── ...
│   │   └── package.json
│   │
│   ├── anthropic/              # Anthropic API 封装
│   │   ├── src/
│   │   │   ├── client.ts
│   │   │   ├── prompts/        # 提示词模板
│   │   │   └── ...
│   │   └── package.json
│   │
│   └── shared/                 # 共享类型和工具
│       ├── src/
│       │   ├── types/
│       │   ├── utils/
│       │   └── ...
│       └── package.json
│
├── assets/                     # 静态资源
├── docs/                       # 文档
├── scripts/                    # 构建脚本
└── package.json (monorepo)
```

---

## 5. 数据模型

### 5.1 本地数据库（SQLite）

#### 5.1.1 conversations（对话表）
```sql
CREATE TABLE conversations (
  id TEXT PRIMARY KEY,
  title TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  project_path TEXT,
  metadata JSON
);
```

#### 5.1.2 messages（消息表）
```sql
CREATE TABLE messages (
  id TEXT PRIMARY KEY,
  conversation_id TEXT REFERENCES conversations(id),
  role TEXT, -- 'user' | 'assistant' | 'system'
  content TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSON,
  FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);
```

#### 5.1.3 code_index（代码索引表）
```sql
CREATE TABLE code_index (
  id TEXT PRIMARY KEY,
  file_path TEXT,
  file_hash TEXT,
  indexed_at TIMESTAMP,
  symbols JSON, -- 符号定义
  ast JSON,     -- AST 摘要
  dependencies JSON
);
```

#### 5.1.4 skills（技能表）
```sql
CREATE TABLE skills (
  id TEXT PRIMARY KEY,
  name TEXT,
  version TEXT,
  description TEXT,
  content TEXT, -- YAML/Markdown
  source TEXT,  -- 'builtin' | 'local' | 'marketplace'
  enabled BOOLEAN DEFAULT false,
  priority INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 5.1.5 task_templates（工作流模板表）
```sql
CREATE TABLE task_templates (
  id TEXT PRIMARY KEY,
  name TEXT,
  description TEXT,
  steps JSON,
  parameters JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5.2 配置文件

#### .claude/config.yaml（项目配置）
```yaml
# Claude Code 项目配置
project:
  name: my-project
  type: typescript

index:
  exclude:
    - node_modules/**
    - dist/**
    - .git/**

skills:
  enabled:
    - react-best-practices
    - typescript-style

privacy:
  send_files: true
  send_all_files: false
  exclude_from_send:
    - .env
    - secrets/**

git:
  auto_commit: true
  auto_branch: false
  commit_prefix: "[claude]"
```

#### ~/.claude/config.yaml（全局配置）
```yaml
# Claude Code 全局配置
user:
  id: "user_123"
  email: "user@example.com"

theme: dark
model: "claude-3-5-sonnet-20241022"

sync:
  enabled: true
  endpoint: "https://api.claude.anthropic.com"

privacy:
  save_history: true
  analytics_enabled: true
```

---

## 6. API 设计

### 6.1 核心内部 API

#### 6.1.1 Chat API（对话）

```typescript
interface ChatService {
  // 创建新对话
  createConversation(options?: {
    projectPath?: string;
    title?: string;
  }): Promise<Conversation>;

  // 发送消息
  sendMessage(
    conversationId: string,
    message: string,
    options?: {
      files?: string[];
      codeSnippet?: string;
    }
  ): Promise<AsyncIterable<MessageChunk>>;

  // 获取对话历史
  getConversation(conversationId: string): Promise<Conversation>;

  // 获取消息列表
  getMessages(conversationId: string): Promise<Message[]>;
}
```

#### 6.1.2 Task API（任务）

```typescript
interface TaskService {
  // 创建任务
  createTask(description: string, options?: {
    projectPath?: string;
    template?: string;
  }): Promise<Task>;

  // 执行任务
  executeTask(taskId: string): Promise<TaskExecution>;

  // 获取任务计划
  getPlan(taskId: string): Promise<TaskPlan>;

  // 确认步骤
  confirmStep(taskId: string, stepId: string): Promise<void>;

  // 跳过步骤
  skipStep(taskId: string, stepId: string): Promise<void>;

  // 取消任务
  cancelTask(taskId: string): Promise<void>;

  // 保存为模板
  saveAsTemplate(taskId: string, name: string): Promise<TaskTemplate>;
}
```

#### 6.1.3 CodeIndex API（代码索引）

```typescript
interface CodeIndexService {
  // 索引代码库
  index(projectPath: string, options?: {
    incremental?: boolean;
    exclude?: string[];
  }): Promise<IndexProgress>;

  // 获取索引状态
  getStatus(projectPath: string): Promise<IndexStatus>;

  // 查询符号
  querySymbols(projectPath: string, query: string): Promise<Symbol[]>;

  // 查找引用
  findReferences(projectPath: string, symbolId: string): Promise<Reference[]>;

  // 获取文件索引
  getFileIndex(projectPath: string, filePath: string): Promise<FileIndex | null>;

  // 询问代码库
  askCodebase(projectPath: string, question: string): Promise<CodebaseAnswer>;
}
```

#### 6.1.4 Skills API（技能）

```typescript
interface SkillsService {
  // 获取所有技能
  listSkills(): Promise<Skill[]>;

  // 获取已启用技能
  getEnabledSkills(projectPath?: string): Promise<Skill[]>;

  // 启用技能
  enableSkill(skillId: string, projectPath?: string): Promise<void>;

  // 禁用技能
  disableSkill(skillId: string, projectPath?: string): Promise<void>;

  // 创建技能
  createSkill(skill: CreateSkillInput): Promise<Skill>;

  // 更新技能
  updateSkill(skillId: string, skill: UpdateSkillInput): Promise<Skill>;

  // 删除技能
  deleteSkill(skillId: string): Promise<void>;

  // 从市场安装
  installFromMarketplace(skillId: string): Promise<Skill>;
}
```

#### 6.1.5 Rollback API（回滚）

```typescript
interface RollbackService {
  // 获取操作历史
  getHistory(projectPath: string, options?: {
    limit?: number;
    since?: Date;
  }): Promise<Operation[]>;

  // 回滚到指定点
  rollbackTo(operationId: string): Promise<void>;

  // 回滚单个操作
  rollbackOperation(operationId: string): Promise<void>;

  // 创建检查点
  createCheckpoint(projectPath: string, description?: string): Promise<Checkpoint>;
}
```

### 6.2 Anthropic API 封装

```typescript
interface AnthropicClient {
  // 发送消息
  createMessage(
    params: CreateMessageParams
  ): Promise<Message>;

  // 流式消息
  createMessageStream(
    params: CreateMessageParams
  ): Promise<AsyncIterable<MessageStreamEvent>>;

  // 带上下文的对话
  chatWithContext(
    messages: ChatMessage[],
    context: ChatContext
  ): Promise<AsyncIterable<MessageChunk>>;
}

// 提示词模板
const PROMPTS = {
  codeUnderstanding: `你是一位专业的代码理解助手。
请分析以下代码库并回答用户问题。

代码库结构：
{{codeStructure}}

相关文件：
{{relevantFiles}}

用户问题：{{question}}`,

  taskPlanning: `你是一位任务规划专家。
请将用户的任务分解为可执行的步骤。

任务描述：{{task}}

代码库上下文：{{context}}

请按以下 JSON 格式输出：
{
  "steps": [
    {
      "id": "step-1",
      "description": "...",
      "type": "edit" | "command" | "create",
      "expectedChanges": "...",
      "risk": "low" | "medium" | "high"
    }
  ]
}`,

  codeReview: `你是一位代码审查专家。
请审查以下代码变更，找出问题并建议改进。

变更内容：
{{diff}}

请指出：
1. 潜在的 bug
2. 代码风格问题
3. 性能问题
4. 安全问题
5. 改进建议`
};
```

---

## 7. 用户故事与验收标准

### 史诗 1：代码库理解

#### US 1.1：首次索引代码库
**作为**开发者，**我希望**Claude 能自动索引我的代码库，**这样**它就能理解我的项目结构。

**验收标准**：
- [ ] 打开项目时自动开始索引
- [ ] 显示索引进度（百分比 + 已处理文件数）
- [ ] 索引完成后通知用户
- [ ] 中型项目（10k 文件）索引 < 5 分钟
- [ ] 索引失败时显示错误信息和重试选项

**优先级**：P0
**估点**：8
**依赖**：无

---

#### US 1.2：询问代码库问题
**作为**开发者，**我希望**用自然语言询问关于代码库的问题，**这样**我就能快速理解架构和流程。

**验收标准**：
- [ ] 可以问"我们这里是如何处理认证的？"这类问题
- [ ] Claude 引用相关代码文件（带链接）
- [ ] 解释清晰易懂
- [ ] 提供具体的代码示例
- [ ] 回答在 10 秒内返回

**优先级**：P0
**估点**：5
**依赖**：US 1.1

---

#### US 1.3：理解团队约定
**作为**团队成员，**我希望**Claude 能学习我们团队的代码风格和约定，**这样**它的建议才符合我们的规范。

**验收标准**：
- [ ] Claude 观察现有代码，推断约定
- [ ] 可以通过 .claude/config.yaml 显式定义约定
- [ ] 建议符合已有的代码风格
- [ ] 可以说明"我看到你们这里倾向于使用 X 模式"
- [ ] 可以查看和编辑已学习的约定

**优先级**：P1
**估点**：5
**依赖**：US 1.1

---

### 史诗 2：多步骤任务自动化

#### US 2.1：描述任务并执行
**作为**开发者，**我希望**用自然语言描述一个任务，让 Claude 规划并执行，**这样**我就不用手动一步步做了。

**验收标准**：
- [ ] 可以说"为 auth 模块写测试"
- [ ] Claude 将任务分解为步骤
- [ ] 显示任务计划供用户确认
- [ ] 每步执行前都可预览
- [ ] 可以随时暂停或取消
- [ ] 支持用户修改计划（添加/删除/重排步骤）

**优先级**：P0
**估点**：13
**依赖**：US 1.1, US 1.2

---

#### US 2.2：测试生成和修复工作流
**作为**开发者，**我希望**Claude 能"生成测试 → 运行 → 修复失败"，**这样**我就能快速获得完整的测试套件。

**验收标准**：
- [ ] 一键启动完整工作流
- [ ] 智能分析测试失败原因
- [ ] 提供多个修复选项供选择
- [ ] 所有变更都可预览
- [ ] 可以在任何步骤中断
- [ ] 最终所有测试通过

**优先级**：P0
**估点**：8
**依赖**：US 2.1

---

#### US 2.3：保存和重用工作流
**作为**开发者，**我希望**保存常用的工作流，**这样**以后就能一键重用。

**验收标准**：
- [ ] 可以将当前任务保存为模板
- [ ] 给工作流起名字和描述
- [ ] 从库中快速选择已保存的工作流
- [ ] 支持参数化模板（占位符变量）
- [ ] 分享工作流给团队（导出/导入）
- [ ] 工作流列表可搜索和排序

**优先级**：P1
**估点**：5
**依赖**：US 2.1

---

### 史诗 3：技能系统

#### US 3.1：使用内置技能
**作为**开发者，**我希望**使用内置的技能（如 React 最佳实践），**这样**Claude 就能给出符合框架约定的建议。

**验收标准**：
- [ ] 浏览技能库（列表/网格视图）
- [ ] 一键激活/停用技能
- [ ] 看到技能生效的证据（提示中包含技能内容）
- [ ] 可以同时激活多个技能（按优先级排序）
- [ ] 技能详细信息页面

**优先级**：P1
**估点**：5
**依赖**：US 1.3

---

#### US 3.2：创建自定义技能
**作为**技术主管，**我希望**创建团队特定的技能，**这样**Claude 就能遵守我们的内部规范。

**验收标准**：
- [ ] 用简单的 YAML/Markdown 格式定义技能
- [ ] 内置技能编辑器（带语法高亮和验证）
- [ ] 可以说"我们这里总是用 X 模式"来创建技能
- [ ] 技能可以只对当前项目生效，或全局生效
- [ ] 可以分享技能给团队
- [ ] 技能版本历史

**优先级**：P1
**估点**：8
**依赖**：US 3.1

---

### 史诗 4：安全和控制

#### US 4.1：预览所有变更
**作为**开发者，**我希望**在应用前预览 Claude 的所有变更，**这样**我就知道它在做什么。

**验收标准**：
- [ ] 所有变更都有清晰的 diff 视图
- [ ] 支持行内 diff 和并排 diff
- [ ] 可以逐变更确认
- [ ] 可以接受/拒绝单个变更
- [ ] diff 高亮显示差异（添加/删除/修改）
- [ ] 批量确认选项

**优先级**：P0
**估点**：5
**依赖**：无

---

#### US 4.2：一键回滚
**作为**开发者，**我希望**一键回滚 Claude 的变更，**这样**出问题时能快速恢复。

**验收标准**：
- [ ] 一个按钮就能撤销所有变更
- [ ] 可以选择性回滚某些变更
- [ ] 回滚后确认状态正确
- [ ] Git 集成（自动创建分支/提交）
- [ ] 操作历史时间线视图
- [ ] 回滚操作在 5 秒内完成

**优先级**：P0
**估点**：5
**依赖**：US 4.1

---

## 8. 冲刺计划

### Sprint 1：基础框架（2 周）

**目标**：建立产品基础架构，完成代码索引核心功能

**用户故事**：
- US 1.1：首次索引代码库（8 点）

**技术任务**：
- [ ] 搭建 monorepo 项目结构
- [ ] 配置 TypeScript、ESLint、Prettier
- [ ] 设计并实现 SQLite 数据模型
- [ ] 集成 Tree-sitter 代码解析
- [ ] 实现基础代码索引器
- [ ] 搭建 CLI 基础框架
- [ ] 搭建 VS Code 扩展基础框架
- [ ] 集成 Anthropic API 客户端

**验收**：
- [ ] 可以索引简单项目（<100 文件）
- [ ] 索引进度显示正常
- [ ] 基础 CLI 可用
- [ ] 基础 VS Code 扩展可安装

---

### Sprint 2：对话和理解（2 周）

**目标**：实现核心对话和代码库理解功能

**用户故事**：
- US 1.2：询问代码库问题（5 点）
- US 4.1：预览所有变更（5 点）
- US 4.2：一键回滚（5 点）

**技术任务**：
- [ ] 实现对话管理服务
- [ ] 实现代码库问答功能
- [ ] 实现 Diff 视图组件
- [ ] 实现变更确认流程
- [ ] 实现回滚引擎
- [ ] Git 集成（分支、提交）
- 提示词工程优化

**验收**：
- [ ] 可以问代码库问题并得到答案
- [ ] 所有变更都可预览
- [ ] 可以一键回滚变更
- [ ] Git 集成正常工作

---

### Sprint 3：多步骤任务（3 周）

**目标**：实现任务自动化核心功能

**用户故事**：
- US 2.1：描述任务并执行（13 点）
- US 2.2：测试生成和修复工作流（8 点）

**技术任务**：
- [ ] 实现任务规划器
- [ ] 实现任务执行引擎
- [ ] 实现步骤预览和确认
- [ ] 实现测试生成工作流
- [ ] 实现测试运行和修复循环
- [ ] 错误处理和恢复
- [ ] 提示词工程（任务分解）

**验收**：
- [ ] 可以描述任务并执行
- [ ] 测试生成工作流可用
- [ ] 任务可以暂停和取消
- [ ] 错误可以恢复

---

### Sprint 4：技能系统（2 周）

**目标**：实现技能系统基础版本

**用户故事**：
- US 3.1：使用内置技能（5 点）
- US 1.3：理解团队约定（5 点）

**技术任务**：
- [ ] 设计技能文件格式（YAML）
- [ ] 实现技能加载和解析
- [ ] 实现技能管理器
- [ ] 实现约定学习算法
- [ ] 技能 UI（浏览器、激活/停用）
- [ ] 创建内置技能库（10-15 个）
- [ ] 技能与提示词集成

**验收**：
- [ ] 可以使用内置技能
- [ ] Claude 理解并遵守团队约定
- [ ] 技能可以激活和停用
- [ ] 可以同时使用多个技能

---

### Sprint 5：打磨和发布（2 周）

**目标**：打磨体验，准备 Beta 发布

**用户故事**：
- US 2.3：保存和重用工作流（5 点）
- US 3.2：创建自定义技能（8 点）

**技术任务**：
- [ ] 实现工作流保存和重用
- [ ] 实现自定义技能创建
- [ ] UX 优化（错误提示、加载状态、空状态）
- [ ] 性能优化（索引速度、响应时间）
- [ ] 错误边界和崩溃恢复
- [ ] Analytics 集成
- [ ] 打包和发布准备
- [ ] 文档（README、使用指南）

**验收**：
- [ ] 所有核心功能可用
- [ ] 性能达标
- [ ] 无严重 bug
- [ ] 准备 Beta 发布

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
- 所有核心服务（ChatService、TaskService、CodeIndexService 等）
- 工具函数
- 数据模型验证
- 提示词模板验证

**框架**：Jest + Testing Library

**目标覆盖率**：> 80%

**示例测试**：
```typescript
describe('CodeIndexService', () => {
  describe('index', () => {
    it('should index a simple project', async () => {
      const service = new CodeIndexService();
      const progress = await service.index('/test/project');

      expect(progress.status).toBe('completed');
      expect(progress.filesIndexed).toBeGreaterThan(0);
    });

    it('should show progress during indexing', async () => {
      const service = new CodeIndexService();
      const progressStream = service.indexStream('/test/project');

      for await (const progress of progressStream) {
        expect(progress.percentage).toBeGreaterThanOrEqual(0);
        expect(progress.percentage).toBeLessThanOrEqual(100);
      }
    });
  });
});
```

### 9.3 集成测试

**覆盖范围**：
- 服务间交互
- 数据库操作
- Anthropic API 集成（使用 mock）
- Git 集成
- VS Code 扩展 API

**框架**：Jest + Supertest（如需要）

**示例测试**：
```typescript
describe('Task + Rollback integration', () => {
  it('should execute a task and be able to rollback', async () => {
    // 创建任务
    const task = await taskService.createTask('Add a test file');

    // 执行任务
    const execution = await taskService.executeTask(task.id);
    expect(execution.status).toBe('completed');

    // 验证文件已创建
    expect(fs.existsSync('/test/project/test.ts')).toBe(true);

    // 回滚
    await rollbackService.rollbackTo(execution.operationId);

    // 验证文件已删除
    expect(fs.existsSync('/test/project/test.ts')).toBe(false);
  });
});
```

### 9.4 E2E 测试

**覆盖范围**：
- 核心用户流程
- 跨平台一致性
- 真实 Anthropic API（使用测试账户）

**框架**：Playwright

**示例测试**：
```typescript
describe('VS Code Extension E2E', () => {
  it('should have a complete conversation flow', async ({ page }) => {
    // 打开 VS Code 测试实例
    await vscode.openWorkspace('/test/project');

    // 打开 Claude 侧边栏
    await page.click('[aria-label="Claude Code"]');

    // 发送消息
    await page.fill('.chat-input', 'What is in this project?');
    await page.click('.send-button');

    // 等待回复
    const response = await page.waitForSelector('.assistant-message');
    expect(await response.textContent()).toContain('project');
  });
});
```

### 9.5 AI 输出测试

**特别策略**：
- 使用 golden master 测试（保存已知好的输出作为基准）
- A/B 测试提示词变更
- 人工审查关键路径输出
- 评分模型：相关性、正确性、安全性

### 9.6 性能测试

**关键指标**：
- 索引时间（不同项目大小）
- API 响应时间（p50, p95, p99）
- 内存占用（空闲、峰值）
- 启动时间（CLI、VS Code）

**工具**：Lighthouse、自定义性能脚本

---

## 10. 监控与指标

### 10.1 产品指标

| 指标 | 目标 | 测量方式 | 警报阈值 |
|------|------|---------|---------|
| 试用→付费转化 | >15% | 计费系统 | <10% |
| 周活跃率 | >60% | 产品分析 | <40% |
| 第 7 天留存 | >50% | 产品分析 | <30% |
| 第 30 天留存 | >30% | 产品分析 | <20% |
| NPS | >40 | 用户调查 | <30 |
| 任务完成率 | >80% | 产品分析 | <60% |
| 代码接受率 | >70% | 产品分析 | <50% |

### 10.2 技术指标

| 指标 | 目标 | 警报阈值 |
|------|------|---------|
| API 错误率 | <5% | >10% |
| API p95 响应时间 | <10s | >15s |
| 索引成功率 | >95% | <90% |
| 崩溃率 | <1% | >5% |
| AI 成本/收入 | <30% | >40% |

### 10.3 护栏指标（Guardrail Metrics）

**用户满意度护栏**：
- [ ] 任务成功率 <70% → 警报
- [ ] 代码接受率 <50% → 警报
- [ ] NPS <30 → 警报

**性能护栏**：
- [ ] 响应时间 p95 >10s → 警报
- [ ] 错误率 >5% → 警报

**成本护栏**：
- [ ] AI 成本/收入 >40% → 警报

**信任护栏**：
- [ ] 回滚使用率 >15% → 警报
- [ ] "信任度"评分 <3.5/5 → 警报

### 10.4 每周指标回顾模板

| 指标 | 上周 | 本周 | 变化 | 评论 |
|------|------|------|------|------|
| 北极星指标 | | | | |
| 周活跃用户 | | | | |
| 平均每周节省时间 | | | | |
| 第 7 天留存 | | | | |
| 试用→付费转化 | | | | |
| MRR | | | | |
| NPS | | | | |
| 任务成功率 | | | | |
| API 错误率 | | | | |
| AI 成本/收入 | | | | |

---

## 11. 风险与依赖

### 11.1 风险登记册

| 风险 | 影响 | 可能性 | 优先级 | 缓解措施 | 负责人 |
|------|------|--------|--------|---------|--------|
| AI 模型性能不达标 | 🔴 严重 | 🟡 中 | P0 | 早期测试，准备降级方案，多个模型备份 | 架构师 |
| 代码索引速度慢 | 🟡 中 | 🟡 中 | P1 | 优化算法，渐进式索引，并行处理 | 后端 |
| 用户信任不足 | 🟡 中 | 🟢 高 | P1 | 强调控制和回滚，透明沟通，安全向导 | PM/设计 |
| Anthropic API 限制 | 🟡 中 | 🟡 中 | P1 | 速率限制处理，缓存，备用 API 密钥 | DevOps |
| VS Code 审核延迟 | 🟡 中 | 🟡 中 | P2 | 提前提交，准备多个版本，官网直接下载 | PM |
| 竞争对手快速跟进 | 🟡 中 | 🟢 高 | P2 | 快速迭代，建立社区和生态，品牌建设 | 全团队 |

### 11.2 依赖项

| 依赖 | 类型 | 重要性 | 预计时间 | 备注 |
|------|------|--------|---------|------|
| Anthropic Claude API 访问 | 外部 | 🔴 关键 | Sprint 1 前 | 已确认 |
| VS Code 扩展市场发布 | 外部 | 🟡 重要 | Beta 前 | 需要审核 |
| 云基础设施（AWS/GCP） | 外部 | 🟡 重要 | Sprint 3 前 | 可选，本地优先 |
| Tree-sitter 多语言支持 | 开源 | 🟡 重要 | Sprint 1 | 已有 |
| 设计资源（UI 组件） | 内部 | 🟢 一般 | Sprint 2 | 按需创建 |

### 11.3 假设清单

| 假设 | 验证方法 | 状态 |
|------|---------|------|
| 开发者愿意为 AI 编程助手支付 $20/月 | 用户访谈、定价测试 | 待验证 |
| "深度理解 + 多步骤自动化"是关键差异化 | 竞品对比测试 | 待验证 |
| 开发者会信任 AI，只要有控制和回滚 | 信任度调查、行为分析 | 待验证 |
| 30 分钟内体验"啊哈！"时刻 | onboarding funnel 分析 | 待验证 |
| 产品主导增长（PLG）有效 | 渠道分析、CAC 测量 | 待验证 |

---

## 附录

### A. 术语表

| 术语 | 定义 |
|------|------|
| TAM | Total Addressable Market，总可服务市场 |
| SAM | Serviceable Available Market，可服务市场 |
| SOM | Serviceable Obtainable Market，可获得市场 |
| PLG | Product-Led Growth，产品主导增长 |
| PMF | Product-Market Fit，产品市场匹配 |
| NPS | Net Promoter Score，净推荐值 |
| CAC | Customer Acquisition Cost，用户获取成本 |
| LTV | Lifetime Value，用户生命周期价值 |
| MVP | Minimum Viable Product，最小可行产品 |
| AST | Abstract Syntax Tree，抽象语法树 |

### B. 参考文档

- [阶段一：AI 战略规划总结](./01_AI战略规划/阶段总结.md)
- [阶段二：AI 市场研究总结](./02_AI市场研究/阶段总结.md)
- [阶段三：AI 产品发现总结](./03_AI产品发现/阶段总结.md)
- [阶段六：AI 市场推广总结](./06_AI市场推广/阶段总结.md)

### C. 变更历史

| 版本 | 日期 | 变更 | 作者 |
|------|------|------|------|
| 1.0 | 2026-03-16 | 初始版本 | AI 产品团队 |

---

**文档结束**

如有疑问，请联系产品团队。
