---
name: knowledge-citadel
description: 知识城邦 - 一个游戏化的个人知识管理系统。当用户想要添加知识、查看知识城邦、管理个人知识库时使用此技能。
---

# 知识城邦 (Knowledge Citadel) Skill

一个游戏化的个人知识管理系统，让用户通过建设虚拟城邦来管理知识。

## 核心概念

| 现实概念 | 游戏化映射 |
|---------|-----------|
| 单条笔记/知识点 | 建筑（图书馆、工坊、灯塔等）|
| 知识分类 | 城区/区域 |
| 知识关联 | 道路、桥梁 |
| 标签 | 装饰、旗帜 |

## 建筑类型

| 类型 | Emoji | 用途 |
|-----|-------|------|
| 图书馆 | 📚 | 理论知识、概念定义 |
| 工坊 | 🏭 | 实操技能、步骤方法 |
| 灯塔 | 💡 | 灵感创意、突发想法 |
| 纪念馆 | 🏛️ | 重要记录、里程碑 |
| 仓库 | 🏪 | 资料素材、参考链接 |

## 数据存储格式

城邦数据使用 Markdown 格式存储在 `knowledge-citadel.md` 文件中。

## 技能触发

当用户说以下内容时，使用此技能：
- "打开知识城邦" / "启动知识城邦"
- "添加知识" / "添加笔记"
- "查看城邦" / "看我的知识城邦"
- "知识城邦"

## 使用流程

### 1. 初始化或加载城邦

首先检查当前目录是否存在 `knowledge-citadel.md` 文件。如果不存在，创建新的城邦；如果存在，加载现有城邦。

使用 `scripts/citadel.py load` 来加载或初始化城邦。

### 2. 主要命令

| 功能 | 脚本调用 |
|-----|---------|
| 添加知识 | `scripts/citadel.py add <title> <content> [--type TYPE] [--district DISTRICT]` |
| 查看城邦 | `scripts/citadel.py view` |
| 列出建筑 | `scripts/citadel.py list` |
| 阅读建筑 | `scripts/citadel.py read <id>` |
| 建立关联 | `scripts/citadel.py link <id1> <id2>` |
| 查看成就 | `scripts/citadel.py achievements` |
| 显示帮助 | `scripts/citadel.py help` |

### 3. 输出格式

使用可视化渲染来展示城邦，包括 ASCII 艺术、Markdown 表格和 Emoji 图标。

## scripts/citadel.py 使用说明

### 添加知识

```bash
python scripts/citadel.py add "Python 基础" "Python 是一种解释型编程语言..." --type library --district "学习区"
```

`--type` 可选值: library, workshop, lighthouse, memorial, warehouse

### 查看城邦

```bash
python scripts/citadel.py view
```

输出城邦的全景视图，包括所有建筑、资源和统计信息。

## 数据文件格式

`knowledge-citadel.md` 采用 Markdown 格式，包含以下部分：

1. 城邦元数据 (YAML frontmatter)
2. 城区列表
3. 建筑列表（每个建筑是一个二级标题）
4. 成就记录

示例：

```markdown
---
name: 我的知识城邦
founded_at: 2024-01-15
resources:
  wisdom_coin: 150
  inspiration: 30
  scroll: 2
  visitor: 5
---

# 知识城邦

## 城区

- 学习区
- 工作区

## 建筑

### 📚 图书馆: Python 基础

| 字段 | 值 |
|-----|----|
| ID | abc123 |
| 城区 | 学习区 |
| 等级 | ⭐⭐ |
| 标签 | 编程, Python |
| 创建于 | 2024-01-15 |

内容：Python 是一种解释型、面向对象的编程语言...
```

## 工作流

1. 用户请求与知识城邦相关的操作
2. 检查并加载/初始化城邦数据
3. 执行相应的操作
4. 渲染并展示结果
5. 保存更新后的数据

## 注意事项

- 总是在操作后自动保存城邦数据
- 使用友好的、游戏化的语言与用户交流
- 提供可视化的城邦展示（ASCII 艺术 + Emoji）
