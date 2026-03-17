"""
知识城邦 - 成就系统
Achievement System for Knowledge Citadel
"""

from dataclasses import dataclass, field
from typing import Dict, List, Callable, Optional
from enum import Enum


class AchievementTier(Enum):
    """成就等级"""
    PRIMARY = "primary"      # 初级
    INTERMEDIATE = "intermediate"  # 中级
    ADVANCED = "advanced"    # 高级
    LEGENDARY = "legendary"  # 传奇


@dataclass
class AchievementReward:
    """成就奖励"""
    wisdom_coin: int = 0
    inspiration: int = 0
    scroll: int = 0


@dataclass
class Achievement:
    """成就定义"""
    id: str
    name: str
    description: str
    tier: AchievementTier
    emoji: str
    reward: AchievementReward
    condition: Callable[["CityStats"], bool]  # type: ignore
    unlocked: bool = False
    unlocked_at: Optional[str] = None

    def check(self, stats: "CityStats") -> bool:  # type: ignore
        """检查是否达成"""
        if self.unlocked:
            return True
        if self.condition(stats):
            self.unlocked = True
            from datetime import datetime
            self.unlocked_at = datetime.now().isoformat()
            return True
        return False

    def to_dict(self) -> dict:
        """序列化"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tier": self.tier.value,
            "emoji": self.emoji,
            "reward": {
                "wisdom_coin": self.reward.wisdom_coin,
                "inspiration": self.reward.inspiration,
                "scroll": self.reward.scroll,
            },
            "unlocked": self.unlocked,
            "unlocked_at": self.unlocked_at,
        }


@dataclass
class CityStats:
    """城邦统计数据"""
    total_buildings: int = 0
    total_links: int = 0
    total_districts: int = 0
    max_buildings_in_district: int = 0
    total_maintains: int = 0
    days_active: int = 1
    total_output: int = 0

    def to_dict(self) -> dict:
        return {
            "total_buildings": self.total_buildings,
            "total_links": self.total_links,
            "total_districts": self.total_districts,
            "max_buildings_in_district": self.max_buildings_in_district,
            "total_maintains": self.total_maintains,
            "days_active": self.days_active,
            "total_output": self.total_output,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CityStats":
        return cls(
            total_buildings=data.get("total_buildings", 0),
            total_links=data.get("total_links", 0),
            total_districts=data.get("total_districts", 0),
            max_buildings_in_district=data.get("max_buildings_in_district", 0),
            total_maintains=data.get("total_maintains", 0),
            days_active=data.get("days_active", 1),
            total_output=data.get("total_output", 0),
        )


def create_achievements() -> List[Achievement]:
    """创建所有成就"""
    return [
        # 初级成就
        Achievement(
            id="first_building",
            name="初来乍到",
            description="添加第一条知识",
            tier=AchievementTier.PRIMARY,
            emoji="🌱",
            reward=AchievementReward(wisdom_coin=50),
            condition=lambda s: s.total_buildings >= 1,
        ),
        Achievement(
            id="ten_buildings",
            name="小有规模",
            description="添加10条知识",
            tier=AchievementTier.PRIMARY,
            emoji="🏘️",
            reward=AchievementReward(wisdom_coin=100, inspiration=20),
            condition=lambda s: s.total_buildings >= 10,
        ),
        # 中级成就
        Achievement(
            id="ten_links",
            name="四通八达",
            description="建立10条关联",
            tier=AchievementTier.INTERMEDIATE,
            emoji="🛤️",
            reward=AchievementReward(inspiration=50, scroll=1),
            condition=lambda s: s.total_links >= 10,
        ),
        Achievement(
            id="district_specialist",
            name="区域专精",
            description="某个分类满20条",
            tier=AchievementTier.INTERMEDIATE,
            emoji="🎯",
            reward=AchievementReward(wisdom_coin=200, inspiration=50),
            condition=lambda s: s.max_buildings_in_district >= 20,
        ),
        # 高级成就
        Achievement(
            id="hundred_buildings",
            name="知识帝国",
            description="添加100条知识",
            tier=AchievementTier.ADVANCED,
            emoji="🏰",
            reward=AchievementReward(wisdom_coin=500, inspiration=200, scroll=3),
            condition=lambda s: s.total_buildings >= 100,
        ),
        Achievement(
            id="five_districts",
            name="智慧之城",
            description="解锁5个区域",
            tier=AchievementTier.ADVANCED,
            emoji="🌆",
            reward=AchievementReward(inspiration=300, scroll=5),
            condition=lambda s: s.total_districts >= 5,
        ),
        # 传奇成就
        Achievement(
            id="five_hundred_buildings",
            name="活的百科",
            description="添加500条知识",
            tier=AchievementTier.LEGENDARY,
            emoji="📚",
            reward=AchievementReward(wisdom_coin=2000, inspiration=1000, scroll=10),
            condition=lambda s: s.total_buildings >= 500,
        ),
        Achievement(
            id="hundred_links",
            name="知识互联",
            description="建立100条关联",
            tier=AchievementTier.LEGENDARY,
            emoji="🕸️",
            reward=AchievementReward(wisdom_coin=1500, inspiration=800, scroll=8),
            condition=lambda s: s.total_links >= 100,
        ),
    ]


@dataclass
class AchievementManager:
    """成就管理器"""
    achievements: List[Achievement] = field(default_factory=create_achievements)
    newly_unlocked: List[Achievement] = field(default_factory=list)

    def check_all(self, stats: CityStats) -> List[Achievement]:
        """检查所有成就，返回新解锁的"""
        self.newly_unlocked = []
        for achievement in self.achievements:
            if not achievement.unlocked and achievement.check(stats):
                self.newly_unlocked.append(achievement)
        return self.newly_unlocked

    def get_unlocked(self) -> List[Achievement]:
        """获取已解锁的成就"""
        return [a for a in self.achievements if a.unlocked]

    def get_locked(self) -> List[Achievement]:
        """获取未解锁的成就"""
        return [a for a in self.achievements if not a.unlocked]

    def get_by_tier(self, tier: AchievementTier) -> List[Achievement]:
        """按等级获取成就"""
        return [a for a in self.achievements if a.tier == tier]

    def to_dict(self) -> dict:
        """序列化"""
        return {
            "achievements": [a.to_dict() for a in self.achievements],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "AchievementManager":
        """反序列化"""
        manager = cls()
        # 恢复成就状态
        saved_achievements = {a["id"]: a for a in data.get("achievements", [])}
        for achievement in manager.achievements:
            if achievement.id in saved_achievements:
                saved = saved_achievements[achievement.id]
                achievement.unlocked = saved.get("unlocked", False)
                achievement.unlocked_at = saved.get("unlocked_at")
        return manager
