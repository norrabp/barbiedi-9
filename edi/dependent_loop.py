from typing import Optional

from constants import (ClaimFilingIndicatorCode, DateTimePeriodFormatQualifier,
                       EntityIdentifierCode, EntityTypeQualifier,
                       PaymentResponsibilityLevelCode,
                       ReferenceIdentificationQualifier,
                       RelationshipToSubscriber, SegmentHeader)
from edi.address_segment import address_segment
from models.claim import Claim
from models.patient import Patient


def dependent_loop(
    dependent: Optional[Patient], hierarchical_levels: list[str]
) -> list[str]:
    content = []
    if dependent and len(hierarchical_levels) > 2:
        # Check there is a dependent and that there is a hierarchical level for the dependent
        content.extend(
            [
                hierarchical_levels[2],
                "*".join(
                    [
                        SegmentHeader.Patient,  # PAT
                        dependent.relationship_to_subscriber_code,
                    ]
                )
                + "~",
                "*".join(
                    [
                        SegmentHeader.Name,  # NM1
                        EntityIdentifierCode.Patient,  # QC
                        EntityTypeQualifier.Person,  # 1
                        dependent.last_name,
                        dependent.first_name,
                    ]
                )
                + "~",
                *address_segment(dependent.address),
                "*".join(
                    [
                        SegmentHeader.Demographics,  # DMG
                        DateTimePeriodFormatQualifier.YYYYMMDD,  # D8
                        dependent.date_of_birth,
                        dependent.gender if dependent.gender else "",
                    ]
                )
                + "~",
            ]
        )

    return content
