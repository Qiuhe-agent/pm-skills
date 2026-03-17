"""
知识城邦 - 资源系统
Resource System for Knowledge Citadel
"""

from dataclasses import dataclass, field
from typing import Dict
from enum import Enum


class ResourceType(Enum):
    """资源类型"""
    WISDOM_COIN = "wisdom_coin"       # 智慧币
    INSPIRATION = "inspiration"       # 灵感精华
    SCROLL = "scroll"                  # 知识卷轴
    VISITOR = "visitor"                # 访客数


@dataclass
class ResourceConfig:
    """资源配置"""
    name: str
    emoji: str
    description: str


# 资源配置
RESOURCE_CONFIGS: Dict[ResourceType, ResourceConfig] = {
    ResourceType.WISDOM_COIN: ResourceConfig(
        name="智慧币",
        emoji="🪙",
        description="录入知识、日常阅读获得，用于建造基础建筑",
    ),
    ResourceType.INSPIRATION: ResourceConfig(
        name="灵感精华",
        emoji="✨",
        description="应用知识、建立关联获得，用于升级建筑",
    ),
    ResourceType.SCROLL: ResourceConfig(
        name="知识卷轴",
        emoji="📖",
        description="完成成就、里程碑获得，用于解锁特殊建筑",
    ),
    ResourceType.VISITOR: ResourceConfig(
        name="访客数",
        emoji="👥",
        description="知识分享、输出获得，提升城邦声望",
    ),
}


@dataclass
class Resources:
    """资源管理器"""
    values: Dict[ResourceType, int] = field(default_factory=dict)

    def __post_init__(self):
        """初始化默认值"""
        for resource_type in ResourceType:
            if resource_type not in self.values:
                self.values[resource_type] = 0

    def get(self, resource_type: ResourceType) -> int:
        """获取资源数量"""
        return self.values.get(resource_type, 0)

    def add(self, resource_type: ResourceType, amount: int) -> bool:
        """增加资源"""
        if amount < 0:
            return False
        self.values[resource_type] = self.values.get(resource_type, 0) + amount
        return True

    def spend(self, resource_type: ResourceType, amount: int) -> bool:
        """消耗资源"""
        if self.get(resource_type) >= amount:
            self.values[resource_type] -= amount
            return True
        return False

    def can_afford(self, resource_type: ResourceType, amount: int) -> bool:
        """检查是否足够"""
        return self.get(resource_type) >= amount

    @property
    def wisdom_coin(self) -> int:
        return self.get(ResourceType.WISDOM_COIN)

    @wisdom_coin.setter
    def wisdom_coin(self, value: int):
        self.values[ResourceType.WISDOM_COIN] = value

    @property
    def inspiration(self) -> int:
        return self.get(ResourceType.INSPIRATION)

    @inspiration.setter
    def inspiration(self, value: int):
        self.values[ResourceType.INSPIRATION] = value

    @property
    def scroll(self) -> int:
        return self.get(ResourceType.SCROLL)

    @scroll.setter
    def scroll(self, value: int):
        self.values[ResourceType.SCROLL] = value

    @property
    def visitor(self) -> int:
        return self.get(ResourceType.VISITOR)

    @visitor.setter
    def visitor(self, value: int):
        self.values[ResourceType.VISITOR] = value

    def to_dict(self) -> dict:
        """序列化"""
        return {rt.value: v for rt, v in self.values.items()}

    @classmethod
    def from_dict(cls, data: dict) -> "Resources":
        """反序列化"""
        values = {}
        for rt in ResourceType:
            if rt.value in data:
                values[rt] = data[rt.value]
        return cls(values=values)

    def __str__(self) -> str:
        """资源显示"""
        parts = []
        for rt in ResourceType:
            config = RESOURCE_CONFIGS[rt]
            parts.append(f"{config.emoji} {config.name}: {self.get(rt)}")
        return " | ".join(parts)
