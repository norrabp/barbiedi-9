from constants import (
    EntityIdentifierCode,
    EntityTypeQualifier,
    PayerIdentifier,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from models.provider import Entity


def entity_segment(
    entity: Entity,
    entity_identifier_code: EntityIdentifierCode,
    reference_identification_qualifier: ReferenceIdentificationQualifier,
) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.Name.value,
                entity_identifier_code.value,
                *(
                    [
                        EntityTypeQualifier.NonPerson.value,
                        entity.organization_name,
                        "",
                    ]
                    if entity.organization_name
                    else [
                        EntityTypeQualifier.Person.value,
                        entity.last_name,
                        entity.first_name,
                    ]
                ),
                "",
                "",
                "",
                reference_identification_qualifier.value,
                entity.npi or PayerIdentifier.WIMCD.value,
            ]
        )
        + "~"
    ]
