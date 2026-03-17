"""
知识城邦 - Knowledge Citadel
一个游戏化的个人知识管理系统
"""

from .city import KnowledgeCitadel, CityStorage, District, ReputationLevel
from .buildings import Building, BuildingType, BUILDING_CONFIGS, suggest_building_type
from .resources import Resources, ResourceType, RESOURCE_CONFIGS
from .achievements import AchievementManager, CityStats, AchievementTier, Achievement

__version__ = "0.1.0"
__all__ = [
    "KnowledgeCitadel",
    "CityStorage",
    "District",
    "ReputationLevel",
    "Building",
    "BuildingType",
    "BUILDING_CONFIGS",
    "suggest_building_type",
    "Resources",
    "ResourceType",
    "RESOURCE_CONFIGS",
    "AchievementManager",
    "CityStats",
    "AchievementTier",
    "Achievement",
]
