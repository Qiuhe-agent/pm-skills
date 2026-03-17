"""
知识城邦 - 城邦状态管理
City State Management for Knowledge Citadel
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Set
from enum import Enum
import json
import uuid
import os

from .buildings import (
    Building, BuildingType, BUILDING_CONFIGS,
    suggest_building_type
)
from .resources import Resources, ResourceType, RESOURCE_CONFIGS
from .achievements import (
    AchievementManager, CityStats, AchievementTier
)


class ReputationLevel(Enum):
    """声望等级"""
    VILLAGE = ("村落", 0)
    TOWN = ("集镇", 10)
    CITY = ("城市", 50)
    METROPOLIS = ("都市", 200)
    KINGDOM = ("王国", 500)

    def __init__(self, name: str, threshold: int):
        self.level_name = name
        self.threshold = threshold

    @classmethod
    def from_visitors(cls, visitors: int) -> "ReputationLevel":
        """根据访客数计算声望等级"""
        levels = [cls.KINGDOM, cls.METROPOLIS, cls.CITY, cls.TOWN, cls.VILLAGE]
        for level in levels:
            if visitors >= level.threshold:
                return level
        return cls.VILLAGE


@dataclass
class District:
    """城区"""
    id: str
    name: str
    description: str = ""
    unlocked: bool = True
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "unlocked": self.unlocked,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "District":
        return cls(
            id=data["id"],
            name=data["name"],
            description=data.get("description", ""),
            unlocked=data.get("unlocked", True),
            created_at=datetime.fromisoformat(data["created_at"]),
        )


@dataclass
class KnowledgeCitadel:
    """知识城邦主类"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "我的知识城邦"
    founded_at: datetime = field(default_factory=datetime.now)

    # 核心数据
    buildings: Dict[str, Building] = field(default_factory=dict)
    districts: Dict[str, District] = field(default_factory=dict)
    resources: Resources = field(default_factory=Resources)
    achievements: AchievementManager = field(default_factory=AchievementManager)
    stats: CityStats = field(default_factory=CityStats)

    # 游戏状态
    last_login: datetime = field(default_factory=datetime.now)
    daily_login_streak: int = 1

    def __post_init__(self):
        """初始化默认城区"""
        if not self.districts:
            self._create_default_districts()

    def _create_default_districts(self):
        """创建默认城区"""
        default_districts = [
            ("学习区", "学习相关的知识"),
            ("工作区", "工作相关的技能"),
            ("生活区", "生活中的点滴"),
            ("创意区", "灵感与创意"),
        ]
        for name, desc in default_districts:
            district = District(
                id=str(uuid.uuid4()),
                name=name,
                description=desc,
            )
            self.districts[district.id] = district

    def add_building(
        self,
        title: str,
        content: str,
        building_type: Optional[BuildingType] = None,
        district_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Building:
        """添加建筑（知识）"""
        # 自动建议建筑类型
        if building_type is None:
            building_type = suggest_building_type(content)

        # 选择城区
        if district_id is None or district_id not in self.districts:
            district_id = next(iter(self.districts.keys()))

        # 创建建筑
        building = Building(
            id=str(uuid.uuid4()),
            building_type=building_type,
            title=title,
            content=content,
            district=district_id,
            tags=tags or [],
        )

        self.buildings[building.id] = building

        # 给予奖励
        config = BUILDING_CONFIGS[building_type]
        self.resources.add(ResourceType.WISDOM_COIN, config.base_cost)

        # 更新统计
        self._update_stats()

        # 检查成就
        newly_unlocked = self.achievements.check_all(self.stats)
        for achievement in newly_unlocked:
            self.resources.add(ResourceType.WISDOM_COIN, achievement.reward.wisdom_coin)
            self.resources.add(ResourceType.INSPIRATION, achievement.reward.inspiration)
            self.resources.add(ResourceType.SCROLL, achievement.reward.scroll)

        return building

    def link_buildings(self, from_id: str, to_id: str) -> bool:
        """建立建筑关联"""
        if from_id not in self.buildings or to_id not in self.buildings:
            return False

        self.buildings[from_id].add_link(to_id)
        self.buildings[to_id].add_link(from_id)

        # 奖励
        self.resources.add(ResourceType.INSPIRATION, 5)

        # 更新统计
        self._update_stats()

        # 检查成就
        newly_unlocked = self.achievements.check_all(self.stats)
        for achievement in newly_unlocked:
            self.resources.add(ResourceType.WISDOM_COIN, achievement.reward.wisdom_coin)
            self.resources.add(ResourceType.INSPIRATION, achievement.reward.inspiration)
            self.resources.add(ResourceType.SCROLL, achievement.reward.scroll)

        return True

    def upgrade_building(self, building_id: str) -> bool:
        """升级建筑"""
        if building_id not in self.buildings:
            return False

        building = self.buildings[building_id]
        upgrade_cost = building.level * 20

        if self.resources.spend(ResourceType.INSPIRATION, upgrade_cost):
            if building.upgrade():
                return True
            else:
                # 退款
                self.resources.add(ResourceType.INSPIRATION, upgrade_cost)
        return False

    def maintain_building(self, building_id: str) -> bool:
        """维护建筑（阅读/复习）"""
        if building_id not in self.buildings:
            return False

        building = self.buildings[building_id]
        building.maintain()

        # 奖励
        self.resources.add(ResourceType.WISDOM_COIN, 3)
        self.stats.total_maintains += 1

        return True

    def add_district(self, name: str, description: str = "") -> District:
        """添加新城区"""
        district = District(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
        )
        self.districts[district.id] = district
        self._update_stats()
        return district

    def get_district_buildings(self, district_id: str) -> List[Building]:
        """获取某个城区的所有建筑"""
        return [b for b in self.buildings.values() if b.district == district_id]

    def _update_stats(self):
        """更新统计数据"""
        self.stats.total_buildings = len(self.buildings)

        # 计算总关联数
        links = set()
        for building in self.buildings.values():
            for linked_id in building.links_to:
                if building.id < linked_id:  # 避免重复计数
                    links.add((building.id, linked_id))
        self.stats.total_links = len(links)

        # 计算城区数
        self.stats.total_districts = len(self.districts)

        # 计算单个城区最多建筑数
        district_counts = {}
        for building in self.buildings.values():
            district_counts[building.district] = district_counts.get(building.district, 0) + 1
        self.stats.max_buildings_in_district = max(district_counts.values()) if district_counts else 0

    @property
    def reputation_level(self) -> ReputationLevel:
        """获取当前声望等级"""
        return ReputationLevel.from_visitors(self.resources.visitor)

    def to_dict(self) -> dict:
        """序列化"""
        return {
            "id": self.id,
            "name": self.name,
            "founded_at": self.founded_at.isoformat(),
            "buildings": {k: v.to_dict() for k, v in self.buildings.items()},
            "districts": {k: v.to_dict() for k, v in self.districts.items()},
            "resources": self.resources.to_dict(),
            "achievements": self.achievements.to_dict(),
            "stats": self.stats.to_dict(),
            "last_login": self.last_login.isoformat(),
            "daily_login_streak": self.daily_login_streak,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "KnowledgeCitadel":
        """反序列化"""
        city = cls(
            id=data.get("id", str(uuid.uuid4())),
            name=data.get("name", "我的知识城邦"),
            founded_at=datetime.fromisoformat(data["founded_at"]) if "founded_at" in data else datetime.now(),
        )

        # 加载建筑
        city.buildings = {
            k: Building.from_dict(v)
            for k, v in data.get("buildings", {}).items()
        }

        # 加载城区
        city.districts = {
            k: District.from_dict(v)
            for k, v in data.get("districts", {}).items()
        }

        # 加载资源
        if "resources" in data:
            city.resources = Resources.from_dict(data["resources"])

        # 加载成就
        if "achievements" in data:
            city.achievements = AchievementManager.from_dict(data["achievements"])

        # 加载统计
        if "stats" in data:
            city.stats = CityStats.from_dict(data["stats"])

        # 加载登录信息
        if "last_login" in data:
            city.last_login = datetime.fromisoformat(data["last_login"])
        if "daily_login_streak" in data:
            city.daily_login_streak = data["daily_login_streak"]

        city._update_stats()
        return city


class CityStorage:
    """城邦存储管理器"""

    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        self.city_file = os.path.join(storage_dir, "city_state.json")
        os.makedirs(storage_dir, exist_ok=True)

    def save(self, city: KnowledgeCitadel) -> bool:
        """保存城邦"""
        try:
            with open(self.city_file, "w", encoding="utf-8") as f:
                json.dump(city.to_dict(), f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False

    def load(self) -> Optional[KnowledgeCitadel]:
        """加载城邦"""
        if not os.path.exists(self.city_file):
            return None
        try:
            with open(self.city_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return KnowledgeCitadel.from_dict(data)
        except Exception as e:
            print(f"加载失败: {e}")
            return None

    def exists(self) -> bool:
        """检查是否存在存档"""
        return os.path.exists(self.city_file)
