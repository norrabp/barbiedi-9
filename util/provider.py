from constants import (
    EntityIdentifierCode,
    EntityTypeQualifier,
    PayerIdentifier,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)


def provider_segment(
    json_data: dict,
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
                        json_data["organizationName"],
                        "",
                    ]
                    if "organizationName" in json_data
                    else [
                        EntityTypeQualifier.Person.value,
                        json_data["lastName"],
                        json_data["firstName"],
                    ]
                ),
                "",
                "",
                "",
                reference_identification_qualifier.value,
                json_data.get("npi", PayerIdentifier.WIMCD.value),
            ]
        )
        + "~"
    ]
