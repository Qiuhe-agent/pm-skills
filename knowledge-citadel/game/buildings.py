"""
知识城邦 - 建筑系统
Building System for Knowledge Citadel
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum


class BuildingType(Enum):
    """建筑类型枚举"""
    LIBRARY = "library"          # 图书馆 - 理论知识
    WORKSHOP = "workshop"        # 工坊 - 实操技能
    LIGHTHOUSE = "lighthouse"    # 灯塔 - 灵感创意
    MEMORIAL = "memorial"        # 纪念馆 - 重要记录
    WAREHOUSE = "warehouse"      # 仓库 - 资料素材


@dataclass
class BuildingConfig:
    """建筑配置"""
    name: str
    emoji: str
    description: str
    base_cost: int
    base_output: int
    max_level: int = 5


# 建筑类型配置
BUILDING_CONFIGS: Dict[BuildingType, BuildingConfig] = {
    BuildingType.LIBRARY: BuildingConfig(
        name="图书馆",
        emoji="📚",
        description="收藏理论知识、概念定义",
        base_cost=10,
        base_output=5,
    ),
    BuildingType.WORKSHOP: BuildingConfig(
        name="工坊",
        emoji="🏭",
        description="记录实操技能、步骤方法",
        base_cost=15,
        base_output=8,
    ),
    BuildingType.LIGHTHOUSE: BuildingConfig(
        name="灯塔",
        emoji="💡",
        description="捕捉灵感创意、突发想法",
        base_cost=8,
        base_output=10,
    ),
    BuildingType.MEMORIAL: BuildingConfig(
        name="纪念馆",
        emoji="🏛️",
        description="保存重要记录、里程碑",
        base_cost=20,
        base_output=3,
    ),
    BuildingType.WAREHOUSE: BuildingConfig(
        name="仓库",
        emoji="🏪",
        description="存储资料素材、参考链接",
        base_cost=12,
        base_output=4,
    ),
}


@dataclass
class Building:
    """建筑实体"""
    id: str
    building_type: BuildingType
    title: str
    content: str
    district: str = "default"
    tags: List[str] = field(default_factory=list)
    level: int = 1
    created_at: datetime = field(default_factory=datetime.now)
    last_maintained: datetime = field(default_factory=datetime.now)
    links_to: List[str] = field(default_factory=list)  # 关联的建筑ID

    @property
    def config(self) -> BuildingConfig:
        """获取建筑配置"""
        return BUILDING_CONFIGS[self.building_type]

    @property
    def emoji(self) -> str:
        """获取建筑emoji"""
        return self.config.emoji

    @property
    def name(self) -> str:
        """获取建筑名称"""
        return self.config.name

    @property
    def output(self) -> int:
        """计算当前产出"""
        return self.config.base_output * self.level

    def upgrade(self) -> bool:
        """升级建筑"""
        if self.level < self.config.max_level:
            self.level += 1
            return True
        return False

    def maintain(self):
        """维护建筑"""
        self.last_maintained = datetime.now()

    def add_link(self, building_id: str):
        """添加关联"""
        if building_id not in self.links_to and building_id != self.id:
            self.links_to.append(building_id)

    def to_dict(self) -> dict:
        """序列化"""
        return {
            "id": self.id,
            "building_type": self.building_type.value,
            "title": self.title,
            "content": self.content,
            "district": self.district,
            "tags": self.tags,
            "level": self.level,
            "created_at": self.created_at.isoformat(),
            "last_maintained": self.last_maintained.isoformat(),
            "links_to": self.links_to,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Building":
        """反序列化"""
        return cls(
            id=data["id"],
            building_type=BuildingType(data["building_type"]),
            title=data["title"],
            content=data["content"],
            district=data.get("district", "default"),
            tags=data.get("tags", []),
            level=data.get("level", 1),
            created_at=datetime.fromisoformat(data["created_at"]),
            last_maintained=datetime.fromisoformat(data["last_maintained"]),
            links_to=data.get("links_to", []),
        )


def suggest_building_type(content: str) -> BuildingType:
    """根据内容建议建筑类型"""
    content_lower = content.lower()

    # 关键词匹配
    workshop_keywords = ["步骤", "方法", "教程", "怎么做", "如何", "操作", "实操", "技能", "step", "how to", "tutorial"]
    library_keywords = ["定义", "概念", "理论", "是什么", "原理", "知识", "concept", "theory", "definition"]
    lighthouse_keywords = ["想法", "灵感", "创意", "设想", "可能", "或许", "idea", "inspiration", "thought"]
    memorial_keywords = ["重要", "里程碑", "纪念", "记录", "难忘", "important", "milestone", "remember"]

    if any(k in content_lower for k in workshop_keywords):
        return BuildingType.WORKSHOP
    elif any(k in content_lower for k in library_keywords):
        return BuildingType.LIBRARY
    elif any(k in content_lower for k in lighthouse_keywords):
        return BuildingType.LIGHTHOUSE
    elif any(k in content_lower for k in memorial_keywords):
        return BuildingType.MEMORIAL

    # 默认仓库
    return BuildingType.WAREHOUSE
