---
name: kc-builder
description: 构建一个可视化的"知识城邦"，将你的知识文件转化为独特的建筑和区域。当用户想要可视化知识管理、构建知识库、创建知识城邦、或者将 Markdown 文件转化为可视化的知识地图时，使用此技能。
---

# kc-builder - 知识城邦构建器

将你的知识文件转化为一个充满想象力的"知识城邦"！每个知识文件成为一座独特的建筑，相关主题聚集为区域，时间线展示知识成长历程。

## 核心概念

- **知识 → 建筑**：每个 .md 文件对应城邦中的一座建筑
- **主题 → 区域**：相关知识聚集在同一区域
- **时间 → 历史**：按创建/修改时间生成时间线
- **对话 → 创造**：通过与 AI 对话来构建和调整城邦

## 工作流程

### 1. 了解用户需求

首先，通过对话了解：
- 用户的知识文件在哪里（默认 `./knowledge/`）
- 用户想要什么样的城邦风格（奇幻、科幻、复古、自然等）
- 是否有现有配置需要加载

### 2. 探索知识文件

读取知识目录下的 Markdown 文件，分析：
- 文件名和内容主题
- 创建/修改时间
- （可选）文件中的 frontmatter 元数据

### 3. 生成城邦规划

作为创意核心，你需要：
- 为每个知识文件构思一个独特的建筑名称和风格
- 将相关知识归类为区域（给区域起酷炫的名字）
- 规划整体布局和时间线

**建筑命名示例**：
- 编程知识 → "代码塔楼"、"算法神殿"
- 文学笔记 → "故事花园"、"诗歌亭阁"
- 技术文档 → "机械工坊"、"数据图书馆"

**区域命名示例**：
- 编程相关 → "硅谷高地"
- 创意写作 → "灵感谷"
- 学习笔记 → "智慧平原"

在规划过程中，与用户互动，确认他们喜欢的方向。

### 4. 生成配置文件

保存城邦配置到两个位置：
1. `kc-builder.json` - 结构化的城邦数据
2. `kc-builder.md` - 人类可读的城邦描述

### 5. 生成可视化 HTML

创建一个美观、可交互的单页 HTML 文件，包含：
- **2D 地图视图**：鸟瞰城邦，点击建筑查看详情
- **时间线视图**：展示知识成长历程
- **建筑详情**：点击建筑显示原始知识内容

HTML 生成策略：
- 优先使用 Tailwind CSS CDN 进行样式
- 使用简单的 JavaScript 实现交互
- 可以嵌入 SVG 绘制建筑和地图
- 保持单文件，无需外部依赖（除 CDN 外）

## 配置文件格式

### kc-builder.json

```json
{
  "version": "1.0",
  "city_name": "用户给城邦起的名字",
  "theme": "风格主题（奇幻/科幻/复古等）",
  "created_at": "ISO 时间戳",
  "updated_at": "ISO 时间戳",
  "districts": [
    {
      "id": "district-1",
      "name": "区域名称",
      "description": "区域描述",
      "color": "#HEX颜色",
      "buildings": [
        {
          "id": "building-1",
          "name": "建筑名称",
          "style": "建筑风格",
          "description": "建筑描述",
          "file_path": "对应的 md 文件路径",
          "created_at": "文件创建时间",
          "updated_at": "文件修改时间",
          "preview": "内容预览"
        }
      ]
    }
  ],
  "timeline": [
    {
      "date": "ISO 日期",
      "event": "事件描述",
      "building_id": "关联的建筑 ID"
    }
  ]
}
```

### kc-builder.md

```markdown
# 城邦名称

## 概述

[城邦的整体描述和主题]

## 区域一览

### [区域名]

[区域描述]

**建筑**：
- 🏛️ [建筑名] - [描述]
- 🏰 [建筑名] - [描述]

## 时间线

- [日期] - [事件]
```

## HTML 输出模板

使用这个结构生成 HTML（可以根据需要调整样式和交互）：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{city_name}} - 知识城邦</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* 自定义样式 */
        .building { cursor: pointer; transition: transform 0.2s; }
        .building:hover { transform: scale(1.1); }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 to-slate-800 text-white min-h-screen">
    <!-- 顶部导航 -->
    <nav class="bg-slate-800 border-b border-slate-700 p-4">
        <div class="max-w-7xl mx-auto flex gap-4">
            <button onclick="showView('map')" class="px-4 py-2 rounded bg-blue-600 hover:bg-blue-700">地图</button>
            <button onclick="showView('timeline')" class="px-4 py-2 rounded bg-slate-700 hover:bg-slate-600">时间线</button>
            <button onclick="showView('list')" class="px-4 py-2 rounded bg-slate-700 hover:bg-slate-600">列表</button>
        </div>
    </nav>

    <!-- 主标题 -->
    <header class="text-center py-8">
        <h1 class="text-4xl font-bold mb-2">{{city_name}}</h1>
        <p class="text-slate-400">知识城邦 · 建于 {{created_at}}</p>
    </header>

    <!-- 地图视图 -->
    <div id="map-view" class="view max-w-6xl mx-auto p-4">
        <!-- SVG 地图将在这里生成 -->
        <div id="city-map" class="bg-slate-800 rounded-xl p-8 min-h-96">
            <!-- 用 SVG 绘制城邦地图 -->
        </div>
    </div>

    <!-- 时间线视图 -->
    <div id="timeline-view" class="view max-w-4xl mx-auto p-4 hidden">
        <!-- 时间线内容 -->
    </div>

    <!-- 列表视图 -->
    <div id="list-view" class="view max-w-4xl mx-auto p-4 hidden">
        <!-- 建筑列表 -->
    </div>

    <!-- 建筑详情弹窗 -->
    <div id="building-modal" class="fixed inset-0 bg-black/50 hidden items-center justify-center z-50">
        <div class="bg-slate-800 rounded-xl p-6 max-w-2xl w-full mx-4 max-h-[80vh] overflow-y-auto">
            <!-- 建筑详情 -->
        </div>
    </div>

    <script>
        // 城邦数据
        const cityData = {{city_data_json}};

        // 视图切换
        function showView(view) {
            document.querySelectorAll('.view').forEach(v => v.classList.add('hidden'));
            document.getElementById(view + '-view').classList.remove('hidden');
        }

        // 初始化
        function init() {
            renderMap();
            renderTimeline();
            renderList();
        }

        // 渲染地图
        function renderMap() {
            // 使用 SVG 绘制地图
        }

        // 渲染时间线
        function renderTimeline() {
            // 渲染时间线
        }

        // 渲染列表
        function renderList() {
            // 渲染列表
        }

        init();
    </script>
</body>
</html>
```

## 交互模式

### 初次使用

1. 问候用户，介绍知识城邦概念
2. 询问知识文件位置（默认 `./knowledge/`）
3. 询问城邦主题风格
4. 探索文件后，提出初步规划方案
5. 根据用户反馈调整
6. 生成配置和 HTML

### 继续编辑

1. 检查是否存在 `kc-builder.json`
2. 如果存在，加载并询问用户想做什么：
   - 添加新建筑/知识
   - 调整布局或风格
   - 重新生成 HTML
3. 根据用户请求进行修改

### 纯对话创作

用户也可以不使用本地文件，纯粹通过对话来"建造"知识城邦：
- 用户描述知识，你构思建筑
- 共同规划区域布局
- 生成想象中的城邦 HTML

## 重要原则

1. **创意优先**：发挥想象力，让城邦充满趣味和个性
2. **用户参与**：多问用户的想法，让他们参与创造过程
3. **逐步迭代**：不要试图一次完美，先出原型再调整
4. **保持简单**：HTML 保持单文件，便于分享和保存
5. **非必要不写脚本**：尽可能直接生成内容，而不是写生成脚本

## 文件输出位置

默认在当前目录下创建：
- `kc-builder.json` - 城邦配置数据
- `kc-builder.md` - 城邦描述文档
- `kc-builder.html` - 可视化页面
