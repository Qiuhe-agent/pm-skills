"""
知识城邦 - 可视化渲染
Visualization for Knowledge Citadel
"""

from typing import List, Dict, Optional
from .city import KnowledgeCitadel, District
from .buildings import Building, BuildingType
from .resources import RESOURCE_CONFIGS, ResourceType
from .achievements import AchievementTier


class CityRenderer:
    """城邦渲染器"""

    # ASCII 建筑图标
    BUILDING_ASCII = {
        BuildingType.LIBRARY: [
            "  /\\  ",
            " /||\\ ",
            "|____|",
            "| [] |",
            "|____|",
        ],
        BuildingType.WORKSHOP: [
            "  __  ",
            " |  | ",
            " |[]| ",
            "|____|",
            "|_!!_|",
        ],
        BuildingType.LIGHTHOUSE: [
            "  /\\  ",
            " |  | ",
            " |** |",
            " |  | ",
            "/____\\",
        ],
        BuildingType.MEMORIAL: [
            "  __  ",
            " /  \\ ",
            "| -- |",
            "|    |",
            "|____|",
        ],
        BuildingType.WAREHOUSE: [
            " ____ ",
            "|    |",
            "| [] |",
            "| [] |",
            "|____|",
        ],
    }

    @classmethod
    def render_city_map(cls, city: KnowledgeCitadel) -> str:
        """渲染城邦地图"""
        lines = []

        # 标题
        lines.append(cls._render_title(city))
        lines.append("")

        # 资源栏
        lines.append(cls._render_resources(city))
        lines.append("")

        # 按分区分组渲染建筑
        for district_id, district in city.districts.items():
            buildings = city.get_district_buildings(district_id)
            if buildings:
                lines.append(cls._render_district(district, buildings))
                lines.append("")

        # 统计信息
        lines.append(cls._render_stats(city))

        return "\n".join(lines)

    @classmethod
    def _render_title(cls, city: KnowledgeCitadel) -> str:
        """渲染标题"""
        reputation = city.reputation_level
        border = "=" * 50
        title = f"🏰 {city.name} - {reputation.level_name} 🏰"
        centered = title.center(50)
        return f"{border}\n{centered}\n{border}"

    @classmethod
    def _render_resources(cls, city: KnowledgeCitadel) -> str:
        """渲染资源栏"""
        parts = ["📦 资源:"]
        for rt in ResourceType:
            config = RESOURCE_CONFIGS[rt]
            value = city.resources.get(rt)
            parts.append(f"{config.emoji}{value}")
        return " ".join(parts)

    @classmethod
    def _render_district(cls, district: District, buildings: List[Building]) -> str:
        """渲染一个城区"""
        lines = []

        # 城区标题
        lines.append(f"━━━ 【{district.name}】━━━")

        if not buildings:
            lines.append("  (空)")
            return "\n".join(lines)

        # 每行显示的建筑数量
        per_row = 3

        # 分组渲染
        for i in range(0, len(buildings), per_row):
            row_buildings = buildings[i:i + per_row]
            # 逐行渲染ASCII艺术
            for line_idx in range(5):  # 每个建筑5行
                line_parts = []
                for building in row_buildings:
                    ascii_art = cls.BUILDING_ASCII.get(
                        building.building_type,
                        cls.BUILDING_ASCII[BuildingType.WAREHOUSE]
                    )
                    line_parts.append(ascii_art[line_idx])
                    line_parts.append("  ")  # 建筑间距
                lines.append("  " + "".join(line_parts))

            # 建筑标题行
            title_parts = []
            for building in row_buildings:
                title = f"{building.emoji} {building.title[:10]}"
                title_parts.append(f"{title:14}")
            lines.append("  " + "".join(title_parts))

            # 建筑等级行
            level_parts = []
            for building in row_buildings:
                stars = "⭐" * building.level
                level_parts.append(f"{stars:14}")
            lines.append("  " + "".join(level_parts))
            lines.append("")

        return "\n".join(lines)

    @classmethod
    def _render_stats(cls, city: KnowledgeCitadel) -> str:
        """渲染统计信息"""
        lines = ["📊 城邦统计:"]
        lines.append(f"   建筑总数: {city.stats.total_buildings}")
        lines.append(f"   关联总数: {city.stats.total_links}")
        lines.append(f"   城区数量: {city.stats.total_districts}")
        lines.append(f"   维护次数: {city.stats.total_maintains}")
        lines.append(f"   建立日期: {city.founded_at.strftime('%Y-%m-%d')}")
        return "\n".join(lines)

    @classmethod
    def render_building_detail(cls, building: Building) -> str:
        """渲染建筑详情"""
        lines = []
        lines.append(f"{building.emoji} 【{building.name}】{building.emoji}")
        lines.append("─" * 40)
        lines.append(f"标题: {building.title}")
        lines.append(f"等级: {'⭐' * building.level}")
        lines.append(f"创建于: {building.created_at.strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"最后维护: {building.last_maintained.strftime('%Y-%m-%d %H:%M')}")
        if building.tags:
            lines.append(f"标签: {', '.join(building.tags)}")
        if building.links_to:
            lines.append(f"关联: {len(building.links_to)} 条")
        lines.append("─" * 40)
        lines.append("内容:")
        lines.append(building.content)
        return "\n".join(lines)

    @classmethod
    def render_achievements(cls, city: KnowledgeCitadel) -> str:
        """渲染成就列表"""
        lines = ["🏆 成就系统 🏆", ""]

        # 按等级分组
        tier_names = {
            AchievementTier.PRIMARY: "🌟 初级成就",
            AchievementTier.INTERMEDIATE: "⭐ 中级成就",
            AchievementTier.ADVANCED: "💫 高级成就",
            AchievementTier.LEGENDARY: "👑 传奇成就",
        }

        for tier in AchievementTier:
            achievements = city.achievements.get_by_tier(tier)
            if achievements:
                lines.append(f"{tier_names[tier]}")
                for a in achievements:
                    status = "✅" if a.unlocked else "🔒"
                    lines.append(f"  {status} {a.emoji} {a.name}: {a.description}")
                lines.append("")

        # 统计
        unlocked = len(city.achievements.get_unlocked())
        total = len(city.achievements.achievements)
        lines.append(f"已解锁: {unlocked}/{total}")

        return "\n".join(lines)

    @classmethod
    def render_new_achievements(cls, achievements: list) -> str:
        """渲染新解锁的成就"""
        if not achievements:
            return ""

        lines = ["", "🎉🎉🎉 成就解锁！🎉🎉🎉", ""]
        for a in achievements:
            lines.append(f"   {a.emoji} {a.name}")
            lines.append(f"      {a.description}")
            if a.reward.wisdom_coin:
                lines.append(f"      奖励: 🪙 {a.reward.wisdom_coin}")
            if a.reward.inspiration:
                lines.append(f"            ✨ {a.reward.inspiration}")
            if a.reward.scroll:
                lines.append(f"            📖 {a.reward.scroll}")
            lines.append("")
        return "\n".join(lines)

    @classmethod
    def render_help(cls) -> str:
        """渲染帮助信息"""
        return """
╔══════════════════════════════════════════════════════════╗
║                    知识城邦 - 命令指南                     ║
╠══════════════════════════════════════════════════════════╣
║  /add       - 添加新知识（建造建筑）                       ║
║  /view      - 查看城邦全景                                 ║
║  /list      - 列出所有建筑                                 ║
║  /read <id> - 阅读/维护建筑                                ║
║  /link <id1> <id2> - 建立两个建筑的关联                   ║
║  /upgrade <id> - 升级建筑                                  ║
║  /districts - 查看所有城区                                 ║
║  /add-district <name> - 添加新城区                         ║
║  /achievements - 查看成就                                  ║
║  /status    - 查看详细状态                                 ║
║  /help      - 显示帮助                                     ║
║  /quit      - 退出游戏                                     ║
╚══════════════════════════════════════════════════════════╝

💡 提示：每条知识都是城邦中的一座建筑，建立关联让城邦更繁荣！
        """
