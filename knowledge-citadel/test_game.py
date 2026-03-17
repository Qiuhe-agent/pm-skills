#!/usr/bin/env python3
"""
知识城邦 - 简单测试脚本
"""

import os
import sys
import tempfile
import shutil

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import (
    KnowledgeCitadel,
    BuildingType,
)
from game.visualization import CityRenderer


def test_game():
    """测试游戏核心功能"""
    print("🏗️  测试知识城邦...")
    print("=" * 50)

    # 创建临时目录
    test_dir = tempfile.mkdtemp()
    print(f"📁 测试目录: {test_dir}")

    try:
        # 1. 创建城邦
        print("\n1. 创建城邦...")
        city = KnowledgeCitadel(name="测试城邦")
        print(f"   ✅ 城邦创建成功: {city.name}")

        # 2. 添加建筑
        print("\n2. 添加建筑...")
        b1 = city.add_building(
            title="Python 基础",
            content="Python 是一种解释型、面向对象的编程语言。定义：使用缩进来组织代码块。",
            building_type=BuildingType.LIBRARY,
            tags=["编程", "Python"],
        )
        print(f"   ✅ 添加了 {b1.emoji} {b1.title}")

        b2 = city.add_building(
            title="如何用 Python 打印 Hello World",
            content="步骤：1. 打开编辑器 2. 输入 print('Hello World') 3. 运行程序",
            building_type=BuildingType.WORKSHOP,
            tags=["教程", "入门"],
        )
        print(f"   ✅ 添加了 {b2.emoji} {b2.title}")

        b3 = city.add_building(
            title="AI 产品想法",
            content="或许可以做一个结合知识管理和游戏化的产品，让学习更有趣！",
            building_type=BuildingType.LIGHTHOUSE,
            tags=["创意", "AI"],
        )
        print(f"   ✅ 添加了 {b3.emoji} {b3.title}")

        # 3. 建立关联
        print("\n3. 建立关联...")
        city.link_buildings(b1.id, b2.id)
        print(f"   ✅ 关联了 {b1.title} <-> {b2.title}")

        # 4. 检查资源
        print("\n4. 资源状态:")
        print(f"   {city.resources}")

        # 5. 升级建筑
        print("\n5. 升级建筑...")
        success = city.upgrade_building(b1.id)
        if success:
            print(f"   ✅ {b1.title} 升级到 Lv.{b1.level}")

        # 6. 渲染测试
        print("\n6. 渲染城邦...")
        renderer = CityRenderer()
        map_output = renderer.render_city_map(city)
        print("\n" + map_output)

        # 7. 检查成就
        print("\n7. 成就状态:")
        unlocked = city.achievements.get_unlocked()
        for a in unlocked:
            print(f"   ✅ {a.emoji} {a.name}")

        print("\n" + "=" * 50)
        print("🎉 所有测试通过！")
        print("=" * 50)

        return True

    finally:
        # 清理
        shutil.rmtree(test_dir)


if __name__ == "__main__":
    test_game()
