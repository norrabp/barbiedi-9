from dataclasses import dataclass
from typing import Optional

from constants import HierarchicalLevelCode, SegmentHeader
from models.claim import Claim


@dataclass
class HierarchicalLevel:
    id: str
    parent_id: Optional[str] = None
    code: HierarchicalLevelCode = HierarchicalLevelCode.InformationSource
    has_children: bool = False


def get_hierarchical_levels(claim: Claim) -> list[str]:
    # TODO: Update to account for more levels
    levels: list[HierarchicalLevel] = []
    billing_level_id = None
    subscriber_level_id = None
    if claim.billing:
        billing_level_id = str(len(levels) + 1)
        levels.append(
            HierarchicalLevel(
                id=billing_level_id,
                code=HierarchicalLevelCode.InformationSource,
                has_children=claim.subscriber is not None,
            )
        )
    if claim.subscriber:
        subscriber_level_id = str(len(levels) + 1)
        levels.append(
            HierarchicalLevel(
                id=subscriber_level_id,
                code=HierarchicalLevelCode.Subscriber,
                parent_id=billing_level_id,
                has_children=claim.dependent is not None,
            )
        )
    if claim.dependent:
        levels.append(
            HierarchicalLevel(
                id=str(len(levels) + 1),
                code=HierarchicalLevelCode.Patient,
                parent_id=subscriber_level_id,
            )
        )
    for level in levels[:-1]:
        level.has_children = True

    return [
        "*".join(
            [
                SegmentHeader.HierarchicalLevels,
                level.id,
                level.parent_id if level.parent_id else "",
                level.code,
                "1" if level.has_children else "0",
            ]
        )
        + "~"
        for level in levels
    ]
