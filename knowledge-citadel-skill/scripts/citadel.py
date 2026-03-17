#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识城邦 - Knowledge Citadel
游戏化个人知识管理系统 - Markdown 存储版本
"""

import argparse
import os
import sys
import re
import uuid
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum

# 设置控制台输出编码为 UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


# ==================== 枚举和配置 ====================

class BuildingType(Enum):
    """建筑类型"""
    LIBRARY = "library"
    WORKSHOP = "workshop"
    LIGHTHOUSE = "lighthouse"
    MEMORIAL = "memorial"
    WAREHOUSE = "warehouse"


@dataclass
class BuildingConfig:
    """建筑配置"""
    name: str
    emoji: str
    description: str


BUILDING_CONFIGS: Dict[BuildingType, BuildingConfig] = {
    BuildingType.LIBRARY: BuildingConfig("图书馆", "📚", "理论知识、概念定义"),
    BuildingType.WORKSHOP: BuildingConfig("工坊", "🏭", "实操技能、步骤方法"),
    BuildingType.LIGHTHOUSE: BuildingConfig("灯塔", "💡", "灵感创意、突发想法"),
    BuildingType.MEMORIAL: BuildingConfig("纪念馆", "🏛️", "重要记录、里程碑"),
    BuildingType.WAREHOUSE: BuildingConfig("仓库", "🏪", "资料素材、参考链接"),
}


class AchievementTier(Enum):
    """成就等级"""
    PRIMARY = "primary"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    LEGENDARY = "legendary"


@dataclass
class Achievement:
    """成就"""
    id: str
    name: str
    description: str
    tier: AchievementTier
    emoji: str
    unlocked: bool = False


ACHIEVEMENTS: List[Achievement] = [
    Achievement("first_building", "初来乍到", "添加第一条知识", AchievementTier.PRIMARY, "🌱"),
    Achievement("ten_buildings", "小有规模", "添加10条知识", AchievementTier.PRIMARY, "🏘️"),
    Achievement("ten_links", "四通八达", "建立10条关联", AchievementTier.INTERMEDIATE, "🛤️"),
    Achievement("hundred_buildings", "知识帝国", "添加100条知识", AchievementTier.ADVANCED, "🏰"),
]


# ==================== 数据类 ====================

@dataclass
class Building:
    """建筑"""
    id: str
    building_type: BuildingType
    title: str
    content: str
    district: str = "学习区"
    tags: List[str] = field(default_factory=list)
    level: int = 1
    created_at: datetime = field(default_factory=datetime.now)
    last_maintained: Optional[datetime] = None
    links_to: List[str] = field(default_factory=list)

    @property
    def config(self) -> BuildingConfig:
        return BUILDING_CONFIGS[self.building_type]

    @property
    def emoji(self) -> str:
        return self.config.emoji

    @property
    def name(self) -> str:
        return self.config.name


@dataclass
class Resources:
    """资源"""
    wisdom_coin: int = 0
    inspiration: int = 0
    scroll: int = 0
    visitor: int = 0


@dataclass
class KnowledgeCitadel:
    """知识城邦"""
    name: str = "我的知识城邦"
    founded_at: datetime = field(default_factory=datetime.now)
    districts: List[str] = field(default_factory=lambda: ["学习区", "工作区", "生活区", "创意区"])
    buildings: Dict[str, Building] = field(default_factory=dict)
    resources: Resources = field(default_factory=Resources)
    achievements: List[Achievement] = field(default_factory=lambda: list(ACHIEVEMENTS))

    @property
    def total_buildings(self) -> int:
        return len(self.buildings)

    @property
    def total_links(self) -> int:
        links = set()
        for b in self.buildings.values():
            for linked_id in b.links_to:
                if b.id < linked_id:
                    links.add((b.id, linked_id))
        return len(links)

    def add_building(self, title: str, content: str, building_type: BuildingType = None,
                     district: str = None, tags: List[str] = None) -> Building:
        if building_type is None:
            building_type = suggest_building_type(content)
        if district is None or district not in self.districts:
            district = self.districts[0]

        building = Building(
            id=str(uuid.uuid4())[:8],
            building_type=building_type,
            title=title,
            content=content,
            district=district,
            tags=tags or [],
        )
        self.buildings[building.id] = building

        # 奖励
        self.resources.wisdom_coin += 10

        # 检查成就
        self._check_achievements()

        return building

    def link_buildings(self, id1: str, id2: str) -> bool:
        if id1 not in self.buildings or id2 not in self.buildings:
            return False
        if id1 == id2:
            return False

        if id2 not in self.buildings[id1].links_to:
            self.buildings[id1].links_to.append(id2)
        if id1 not in self.buildings[id2].links_to:
            self.buildings[id2].links_to.append(id1)

        self.resources.inspiration += 5
        self._check_achievements()
        return True

    def _check_achievements(self):
        for a in self.achievements:
            if a.unlocked:
                continue
            if a.id == "first_building" and self.total_buildings >= 1:
                a.unlocked = True
            elif a.id == "ten_buildings" and self.total_buildings >= 10:
                a.unlocked = True
            elif a.id == "ten_links" and self.total_links >= 10:
                a.unlocked = True
            elif a.id == "hundred_buildings" and self.total_buildings >= 100:
                a.unlocked = True


def suggest_building_type(content: str) -> BuildingType:
    """根据内容建议建筑类型"""
    content_lower = content.lower()
    workshop_keywords = ["步骤", "方法", "教程", "怎么做", "如何", "操作", "实操", "技能", "step", "how to"]
    library_keywords = ["定义", "概念", "理论", "是什么", "原理", "知识", "concept", "theory", "definition"]
    lighthouse_keywords = ["想法", "灵感", "创意", "设想", "可能", "或许", "idea", "inspiration"]

    if any(k in content_lower for k in workshop_keywords):
        return BuildingType.WORKSHOP
    elif any(k in content_lower for k in library_keywords):
        return BuildingType.LIBRARY
    elif any(k in content_lower for k in lighthouse_keywords):
        return BuildingType.LIGHTHOUSE
    return BuildingType.WAREHOUSE


# ==================== Markdown 存储 ====================

def save_to_markdown(city: KnowledgeCitadel, filepath: str = "knowledge-citadel.md"):
    """保存到 Markdown 文件"""
    lines = []

    # Frontmatter
    lines.append("---")
    lines.append(f"name: {city.name}")
    lines.append(f"founded_at: {city.founded_at.strftime('%Y-%m-%d')}")
    lines.append("resources:")
    lines.append(f"  wisdom_coin: {city.resources.wisdom_coin}")
    lines.append(f"  inspiration: {city.resources.inspiration}")
    lines.append(f"  scroll: {city.resources.scroll}")
    lines.append(f"  visitor: {city.resources.visitor}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {city.name}")
    lines.append("")

    # 城区
    lines.append("## 城区")
    lines.append("")
    for d in city.districts:
        lines.append(f"- {d}")
    lines.append("")

    # 建筑
    lines.append("## 建筑")
    lines.append("")
    for building in city.buildings.values():
        lines.append(f"### {building.emoji} {building.name}: {building.title}")
        lines.append("")
        lines.append("| 字段 | 值 |")
        lines.append("|-----|----|")
        lines.append(f"| ID | {building.id} |")
        lines.append(f"| 类型 | {building.name} |")
        lines.append(f"| 城区 | {building.district} |")
        lines.append(f"| 等级 | {'⭐' * building.level} |")
        lines.append(f"| 标签 | {', '.join(building.tags) if building.tags else '-'} |")
        lines.append(f"| 创建于 | {building.created_at.strftime('%Y-%m-%d')} |")
        if building.links_to:
            lines.append(f"| 关联 | {', '.join(building.links_to)} |")
        lines.append("")
        lines.append("#### 内容")
        lines.append("")
        lines.append(building.content)
        lines.append("")
        lines.append("---")
        lines.append("")

    # 成就
    lines.append("## 成就")
    lines.append("")
    for a in city.achievements:
        status = "✅" if a.unlocked else "🔒"
        lines.append(f"- {status} {a.emoji} **{a.name}**: {a.description}")
    lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def load_from_markdown(filepath: str = "knowledge-citadel.md") -> Optional[KnowledgeCitadel]:
    """从 Markdown 文件加载"""
    if not os.path.exists(filepath):
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    city = KnowledgeCitadel()

    # 解析 frontmatter
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if frontmatter_match:
        fm = frontmatter_match.group(1)
        name_match = re.search(r'name:\s*(.*)', fm)
        if name_match:
            city.name = name_match.group(1).strip()
        founded_match = re.search(r'founded_at:\s*(.*)', fm)
        if founded_match:
            try:
                city.founded_at = datetime.strptime(founded_match.group(1).strip(), "%Y-%m-%d")
            except:
                pass
        # 资源
        for key in ["wisdom_coin", "inspiration", "scroll", "visitor"]:
            m = re.search(fr'{key}:\s*(\d+)', fm)
            if m:
                setattr(city.resources, key, int(m.group(1)))

    # 解析城区
    districts_section = re.search(r'## 城区\n\n(.*?)\n\n##', content, re.DOTALL)
    if districts_section:
        districts = []
        for line in districts_section.group(1).split("\n"):
            if line.strip().startswith("- "):
                districts.append(line.strip()[2:])
        if districts:
            city.districts = districts

    # 解析建筑
    building_sections = re.findall(r'### (.*?)\n\n\| 字段 \| 值 \|(.*?)(?=\n---|\n## |\Z)', content, re.DOTALL)
    for title_part, table_content in building_sections:
        # 提取 emoji 和标题
        emoji_map = {v.emoji: k for k, v in BUILDING_CONFIGS.items()}
        building_type = BuildingType.WAREHOUSE
        title = title_part
        for emoji, bt in emoji_map.items():
            if emoji in title_part:
                building_type = bt
                title = title_part.replace(emoji, "").replace(f"{BUILDING_CONFIGS[bt].name}:", "").strip()
                break

        # 解析表格
        id_match = re.search(r'\| ID \| ([^|]+) \|', table_content)
        district_match = re.search(r'\| 城区 \| ([^|]+) \|', table_content)
        tags_match = re.search(r'\| 标签 \| ([^|]+) \|', table_content)
        created_match = re.search(r'\| 创建于 \| ([^|]+) \|', table_content)
        links_match = re.search(r'\| 关联 \| ([^|]+) \|', table_content)

        # 解析内容
        building_id = id_match.group(1).strip() if id_match else str(uuid.uuid4())[:8]
        district = district_match.group(1).strip() if district_match else city.districts[0]
        tags = []
        if tags_match:
            tag_str = tags_match.group(1).strip()
            if tag_str != "-":
                tags = [t.strip() for t in tag_str.split(",")]
        created_at = datetime.now()
        if created_match:
            try:
                created_at = datetime.strptime(created_match.group(1).strip(), "%Y-%m-%d")
            except:
                pass
        links_to = []
        if links_match:
            links_str = links_match.group(1).strip()
            links_to = [l.strip() for l in links_str.split(",")]

        # 提取内容部分
        content_match = re.search(fr'### {re.escape(title_part)}\n.*?#### 内容\n\n(.*?)(?=\n---|\n### |\Z)', content, re.DOTALL)
        building_content = content_match.group(1).strip() if content_match else ""

        building = Building(
            id=building_id,
            building_type=building_type,
            title=title,
            content=building_content,
            district=district,
            tags=tags,
            created_at=created_at,
            links_to=links_to,
        )
        city.buildings[building.id] = building

    # 解析成就
    achievements_section = re.search(r'## 成就\n\n(.*?)(?=\Z)', content, re.DOTALL)
    if achievements_section:
        for a in city.achievements:
            if f"**{a.name}**" in achievements_section.group(1):
                if "✅" in achievements_section.group(1).split(f"**{a.name}**")[0].split("\n")[-1]:
                    a.unlocked = True

    return city


# ==================== 可视化 ====================

def render_city(city: KnowledgeCitadel) -> str:
    """渲染城邦"""
    lines = []

    # 标题
    border = "=" * 60
    lines.append(border)
    lines.append(f"🏰 {city.name} 🏰".center(60))
    lines.append(border)
    lines.append("")

    # 资源
    lines.append(f"📦 资源: 🪙{city.resources.wisdom_coin}  ✨{city.resources.inspiration}  📖{city.resources.scroll}  👥{city.resources.visitor}")
    lines.append("")

    # 按城区分组
    for district in city.districts:
        district_buildings = [b for b in city.buildings.values() if b.district == district]
        if district_buildings:
            lines.append(f"━━━ 【{district}】━━━")
            for b in district_buildings:
                links = f" 🔗{len(b.links_to)}" if b.links_to else ""
                lines.append(f"  [{b.id}] {b.emoji} {b.title} {'⭐'*b.level}{links}")
            lines.append("")

    # 统计
    lines.append(f"📊 统计: 建筑{city.total_buildings}座 | 关联{city.total_links}条 | 建立于{city.founded_at.strftime('%Y-%m-%d')}")

    # 新成就
    new_achievements = [a for a in city.achievements if a.unlocked]
    if new_achievements:
        lines.append("")
        lines.append("🏆 成就: " + " ".join([f"{a.emoji}{a.name}" for a in new_achievements[:5]]))

    return "\n".join(lines)


def render_building(building: Building) -> str:
    """渲染建筑详情"""
    lines = []
    lines.append(f"{building.emoji} 【{building.name}】{building.emoji}")
    lines.append("─" * 40)
    lines.append(f"标题: {building.title}")
    lines.append(f"ID: {building.id}")
    lines.append(f"城区: {building.district}")
    lines.append(f"等级: {'⭐' * building.level}")
    lines.append(f"创建于: {building.created_at.strftime('%Y-%m-%d')}")
    if building.tags:
        lines.append(f"标签: {', '.join(building.tags)}")
    if building.links_to:
        lines.append(f"关联: {', '.join(building.links_to)}")
    lines.append("─" * 40)
    lines.append("内容:")
    lines.append(building.content)
    return "\n".join(lines)


# ==================== 命令行 ====================

def main():
    parser = argparse.ArgumentParser(description="知识城邦 - Knowledge Citadel")
    subparsers = parser.add_subparsers(title="命令", dest="command")

    # load 命令
    parser_load = subparsers.add_parser("load", help="加载或初始化城邦")

    # add 命令
    parser_add = subparsers.add_parser("add", help="添加知识")
    parser_add.add_argument("title", help="标题")
    parser_add.add_argument("content", help="内容")
    parser_add.add_argument("--type", help="建筑类型 (library/workshop/lighthouse/memorial/warehouse)")
    parser_add.add_argument("--district", help="城区")
    parser_add.add_argument("--tags", help="标签 (逗号分隔)")

    # view 命令
    parser_view = subparsers.add_parser("view", help="查看城邦")

    # list 命令
    parser_list = subparsers.add_parser("list", help="列出所有建筑")

    # read 命令
    parser_read = subparsers.add_parser("read", help="阅读建筑")
    parser_read.add_argument("id", help="建筑ID")

    # link 命令
    parser_link = subparsers.add_parser("link", help="建立关联")
    parser_link.add_argument("id1", help="建筑1 ID")
    parser_link.add_argument("id2", help="建筑2 ID")

    # achievements 命令
    parser_achievements = subparsers.add_parser("achievements", help="查看成就")

    # help 命令
    parser_help = subparsers.add_parser("help", help="显示帮助")

    args = parser.parse_args()

    filepath = "knowledge-citadel.md"

    if args.command == "help":
        parser.print_help()
        return

    # 加载或创建城邦
    city = load_from_markdown(filepath)
    if city is None:
        city = KnowledgeCitadel()
        print(f"🌟 创建新城邦: {city.name}")
    else:
        print(f"🏰 加载城邦: {city.name}")

    if args.command == "load" or args.command is None:
        print("\n" + render_city(city))

    elif args.command == "add":
        building_type = None
        if args.type:
            type_map = {bt.value: bt for bt in BuildingType}
            if args.type in type_map:
                building_type = type_map[args.type]
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
        building = city.add_building(args.title, args.content, building_type, args.district, tags)
        print(f"\n✅ 成功！{building.emoji} {building.name} 已建成！")
        print(f"🪙 获得 10 智慧币！")
        print("\n" + render_city(city))

    elif args.command == "view":
        print("\n" + render_city(city))

    elif args.command == "list":
        print("\n📋 建筑列表:")
        print("─" * 40)
        if not city.buildings:
            print("(还没有建筑，使用 add 命令来建造第一座吧！)")
        else:
            for b in city.buildings.values():
                print(f"[{b.id}] {b.emoji} {b.title} ({b.district})")

    elif args.command == "read":
        matched = None
        for bid in city.buildings:
            if bid.startswith(args.id) or bid == args.id:
                matched = bid
                break
        if matched and matched in city.buildings:
            print("\n" + render_building(city.buildings[matched]))
        else:
            print("❌ 找不到该建筑")

    elif args.command == "link":
        bid1, bid2 = None, None
        for bid in city.buildings:
            if bid.startswith(args.id1) or bid == args.id1:
                bid1 = bid
            if bid.startswith(args.id2) or bid == args.id2:
                bid2 = bid
        if bid1 and bid2:
            if city.link_buildings(bid1, bid2):
                b1 = city.buildings[bid1]
                b2 = city.buildings[bid2]
                print(f"\n✅ {b1.emoji}《{b1.title}》 和 {b2.emoji}《{b2.title}》 已建立关联！")
                print("✨ +5 灵感精华！")
            else:
                print("❌ 关联失败")
        else:
            print("❌ 找不到建筑")

    elif args.command == "achievements":
        print("\n🏆 成就系统:")
        print("─" * 40)
        for a in city.achievements:
            status = "✅" if a.unlocked else "🔒"
            print(f"{status} {a.emoji} {a.name}: {a.description}")

    # 保存
    save_to_markdown(city, filepath)


if __name__ == "__main__":
    main()
