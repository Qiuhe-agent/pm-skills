#!/usr/bin/env python3
"""
知识城邦 - Knowledge Citadel
游戏化个人知识管理系统
"""

import os
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import (
    KnowledgeCitadel,
    CityStorage,
    BuildingType,
    suggest_building_type,
)
from game.visualization import CityRenderer


class KnowledgeCitadelGame:
    """知识城邦游戏主类"""

    def __init__(self, storage_dir: str = None):
        if storage_dir is None:
            storage_dir = os.path.join(os.path.dirname(__file__), "storage")
        self.storage_dir = storage_dir
        self.storage = CityStorage(storage_dir)
        self.city = None
        self.renderer = CityRenderer()
        self._load_or_create_city()

    def _load_or_create_city(self):
        """加载或创建城邦"""
        if self.storage.exists():
            self.city = self.storage.load()
            if self.city:
                print("🏰 欢迎回到知识城邦！")
        else:
            self.city = KnowledgeCitadel()
            print("🌟 欢迎来到知识荒原！让我们开始建设你的知识城邦吧！")
            self._save()

    def _save(self):
        """保存游戏"""
        self.storage.save(self.city)

    def run(self):
        """运行游戏主循环"""
        print(self.renderer.render_help())
        print("\n" + "=" * 50)
        print(self.renderer.render_city_map(self.city))

        while True:
            try:
                cmd = input("\n📜 输入命令 (/help 查看帮助): ").strip()

                if not cmd:
                    continue

                if cmd.startswith("/"):
                    self._handle_command(cmd)
                else:
                    print("❓ 未知输入，请使用 /help 查看命令列表")

            except KeyboardInterrupt:
                print("\n👋 再见！")
                self._save()
                break
            except Exception as e:
                print(f"❌ 错误: {e}")

    def _handle_command(self, cmd: str):
        """处理命令"""
        parts = cmd.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "/add":
            self._cmd_add()
        elif command == "/view":
            self._cmd_view()
        elif command == "/list":
            self._cmd_list()
        elif command == "/read":
            self._cmd_read(args)
        elif command == "/link":
            self._cmd_link(args)
        elif command == "/upgrade":
            self._cmd_upgrade(args)
        elif command == "/districts":
            self._cmd_districts()
        elif command == "/add-district":
            self._cmd_add_district(args)
        elif command == "/achievements":
            self._cmd_achievements()
        elif command == "/status":
            self._cmd_status()
        elif command == "/help":
            print(self.renderer.render_help())
        elif command == "/quit":
            print("👋 再见！")
            self._save()
            sys.exit(0)
        else:
            print("❓ 未知命令，请使用 /help 查看命令列表")

    def _cmd_add(self):
        """添加知识"""
        print("\n📝 建造新建筑")
        print("─" * 30)

        title = input("📌 标题: ").strip()
        if not title:
            print("❌ 标题不能为空")
            return

        print("📝 内容 (输入完成后按 Ctrl+Z 或 Ctrl+D，Windows下按两次回车):")
        content_lines = []
        try:
            while True:
                line = input()
                content_lines.append(line)
        except (EOFError, KeyboardInterrupt):
            pass
        content = "\n".join(content_lines).strip()

        if not content:
            print("❌ 内容不能为空")
            return

        # 建议建筑类型
        suggested_type = suggest_building_type(content)

        print("\n🏗️ 选择建筑类型:")
        for i, bt in enumerate(BuildingType, 1):
            from game.buildings import BUILDING_CONFIGS
            config = BUILDING_CONFIGS[bt]
            marker = " (推荐)" if bt == suggested_type else ""
            print(f"{i}. {config.emoji} {config.name} - {config.description}{marker}")

        type_choice = input(f"\n选择类型 (1-5，默认按推荐): ").strip()

        building_type = suggested_type
        if type_choice.isdigit():
            idx = int(type_choice) - 1
            types = list(BuildingType)
            if 0 <= idx < len(types):
                building_type = types[idx]

        # 选择城区
        print("\n🗺️ 选择城区:")
        districts = list(self.city.districts.items())
        for i, (did, district) in enumerate(districts, 1):
            print(f"{i}. {district.name}")

        district_choice = input(f"\n选择城区 (1-{len(districts)}，默认1): ").strip()

        district_id = districts[0][0]
        if district_choice.isdigit():
            idx = int(district_choice) - 1
            if 0 <= idx < len(districts):
                district_id = districts[idx][0]

        # 标签
        tags_input = input("🏷️ 标签 (逗号分隔，可选): ").strip()
        tags = [t.strip() for t in tags_input.split(",")] if tags_input else []

        # 创建建筑
        building = self.city.add_building(
            title=title,
            content=content,
            building_type=building_type,
            district_id=district_id,
            tags=tags,
        )

        self._save()

        print(f"\n✅ 成功！{building.emoji} {building.name} 已建成！")
        from game.buildings import BUILDING_CONFIGS
        reward = BUILDING_CONFIGS[building_type].base_cost
        print(f"🪙 获得 {reward} 智慧币！")

        # 检查新成就
        if self.city.achievements.newly_unlocked:
            print(self.renderer.render_new_achievements(self.city.achievements.newly_unlocked))
            self._save()

    def _cmd_view(self):
        """查看城邦"""
        print("\n" + self.renderer.render_city_map(self.city))

    def _cmd_list(self):
        """列出所有建筑"""
        print("\n📋 建筑列表")
        print("─" * 50)

        if not self.city.buildings:
            print("(还没有建筑，使用 /add 来建造第一座吧！)")
            return

        for idx, (bid, building) in enumerate(self.city.buildings.items(), 1):
            district = self.city.districts.get(building.district)
            district_name = district.name if district else "未知"
            stars = "⭐" * building.level
            print(f"{idx}. [{bid[:8]}] {building.emoji} {building.title} ({district_name}) {stars}")

    def _cmd_read(self, args):
        """阅读/维护建筑"""
        if not args:
            print("❌ 请指定建筑ID，使用 /list 查看")
            return

        building_id = args[0]

        # 支持短ID匹配
        matched = None
        for bid in self.city.buildings:
            if bid.startswith(building_id) or bid == building_id:
                matched = bid
                break

        if not matched:
            print("❌ 找不到该建筑")
            return

        building = self.city.buildings[matched]
        print("\n" + self.renderer.render_building_detail(building))

        # 维护
        self.city.maintain_building(matched)
        self._save()
        print("\n✨ 建筑已维护！+3 🪙")

    def _cmd_link(self, args):
        """建立关联"""
        if len(args) < 2:
            print("❌ 请指定两个建筑ID")
            return

        id1, id2 = args[0], args[1]

        # 匹配
        bid1, bid2 = None, None
        for bid in self.city.buildings:
            if bid.startswith(id1) or bid == id1:
                bid1 = bid
            if bid.startswith(id2) or bid == id2:
                bid2 = bid

        if not bid1 or not bid2:
            print("❌ 找不到建筑")
            return

        if bid1 == bid2:
            print("❌ 不能关联自己")
            return

        if self.city.link_buildings(bid1, bid2):
            b1 = self.city.buildings[bid1]
            b2 = self.city.buildings[bid2]
            self._save()
            print(f"\n✅ {b1.emoji}《{b1.title}》 和 {b2.emoji}《{b2.title}》 已建立关联！")
            print("✨ +5 灵感精华！")

            if self.city.achievements.newly_unlocked:
                print(self.renderer.render_new_achievements(self.city.achievements.newly_unlocked))
                self._save()

    def _cmd_upgrade(self, args):
        """升级建筑"""
        if not args:
            print("❌ 请指定建筑ID")
            return

        building_id = args[0]

        matched = None
        for bid in self.city.buildings:
            if bid.startswith(building_id):
                matched = bid
                break

        if not matched:
            print("❌ 找不到建筑")
            return

        building = self.city.buildings[matched]
        cost = building.level * 20

        print(f"\n{building.emoji} {building.title} 当前等级: {'⭐' * building.level}")
        print(f"升级到 Lv.{building.level + 1} 需要: ✨ {cost}")

        confirm = input("确认升级? (y/n): ").strip().lower()
        if confirm != 'y':
            print("取消升级")
            return

        if self.city.upgrade_building(matched):
            self._save()
            print(f"\n✅ {building.title} 已升级到 Lv.{building.level}！")
        else:
            print("❌ 升级失败，灵感精华不足或已达最高等级")

    def _cmd_districts(self):
        """查看城区"""
        print("\n🗺️ 城区列表")
        print("─" * 30)
        for did, district in self.city.districts.items():
            count = len(self.city.get_district_buildings(did))
            print(f"📌 {district.name}: {count} 座建筑")
            if district.description:
                print(f"   {district.description}")
            print()

    def _cmd_add_district(self, args):
        """添加城区"""
        if not args:
            name = input("📌 新城区名称: ").strip()
        else:
            name = " ".join(args)

        if not name:
            print("❌ 名称不能为空")
            return

        desc = input("📝 描述 (可选): ").strip()
        district = self.city.add_district(name, desc)
        self._save()
        print(f"\n✅ 新城区「{district.name}」已创建！")

    def _cmd_achievements(self):
        """查看成就"""
        print("\n" + self.renderer.render_achievements(self.city))

    def _cmd_status(self):
        """查看状态"""
        print("\n" + "=" * 50)
        print(self.renderer.render_city_map(self.city))
        print("\n" + "=" * 50)
        print(self.renderer.render_achievements(self.city))


def main():
    """主函数"""
    storage_path = os.path.join(os.path.dirname(__file__), "storage")
    game = KnowledgeCitadelGame(storage_path)
    game.run()


if __name__ == "__main__":
    main()
