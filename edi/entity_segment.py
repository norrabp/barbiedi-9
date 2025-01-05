from constants import (EntityIdentifierCode, EntityTypeQualifier,
                       PayerIdentifier, ReferenceIdentificationQualifier,
                       SegmentHeader)
from models.entity import Entity


def entity_segment(
    entity: Entity,
    entity_identifier_code: EntityIdentifierCode,
    reference_identification_qualifier: ReferenceIdentificationQualifier,
) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.Name,  # NM1
                entity_identifier_code,
                *(
                    [
                        EntityTypeQualifier.NonPerson,  # 2
                        entity.organization_name,
                        "",
                    ]
                    if entity.organization_name
                    else [
                        EntityTypeQualifier.Person,  # 1
                        entity.last_name,
                        entity.first_name,
                    ]
                ),
                "",
                "",
                "",
                reference_identification_qualifier,
                entity.npi or PayerIdentifier.WIMCD,  # WIMCD
            ]
        )
        + "~"
    ]
