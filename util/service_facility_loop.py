from constants import (
    EntityIdentifierCode,
    EntityTypeQualifier,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from models.service_facility_location import ServiceFacilityLocation
from util.address_segment import address_segment


def service_facility_loop(service_facility: ServiceFacilityLocation) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.Name.value,
                EntityIdentifierCode.ServiceFacility.value,
                EntityTypeQualifier.NonPerson.value,
                service_facility.organization_name,
                "",
                "",
                "",
                "",
                ReferenceIdentificationQualifier.NationalProviderIdentifier.value,
                service_facility.npi,
            ]
        )
        + "~",
        *address_segment(service_facility.address),
    ]
