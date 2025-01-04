from constants import (
    EntityIdentifierCode,
    EntityTypeQualifier,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from util.address import address_segment


def service_facility_loop(json_data: dict) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.Name.value,
                EntityIdentifierCode.ServiceFacility.value,
                EntityTypeQualifier.NonPerson.value,
                json_data["claimInformation"]["serviceFacilityLocation"][
                    "organizationName"
                ],
                "",
                "",
                "",
                "",
                ReferenceIdentificationQualifier.NationalProviderIdentifier.value,
                json_data["claimInformation"]["serviceFacilityLocation"]["npi"],
            ]
        )
        + "~",
        *address_segment(json_data["claimInformation"]["serviceFacilityLocation"]["address"])
    
    ]
