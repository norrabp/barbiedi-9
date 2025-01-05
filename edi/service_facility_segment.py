from constants import (EntityIdentifierCode, EntityTypeQualifier,
                       ReferenceIdentificationQualifier, SegmentHeader)
from edi.address_segment import address_segment
from models.claim import Claim


def service_facility_segment(claim: Claim) -> list[str]:
    content = []
    if (
        claim.claim_information.service_facility_location.address
        != claim.billing.address
    ):
        # If the address for the service facility location is different than the billing address
        content.extend(
            [
                "*".join(
                    [
                        SegmentHeader.Name,  # NM1
                        EntityIdentifierCode.ServiceFacility,  # 77
                        EntityTypeQualifier.NonPerson,  # 2
                        claim.claim_information.service_facility_location.organization_name,
                        "",
                        "",
                        "",
                        "",
                        ReferenceIdentificationQualifier.NationalProviderIdentifier,  # XX
                        claim.claim_information.service_facility_location.npi,
                    ]
                )
                + "~",
                *address_segment(
                    claim.claim_information.service_facility_location.address
                ),
            ]
        )
    return content
