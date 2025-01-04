from constants import (
    EntityTypeQualifier,
    SegmentHeader,
    ProviderType,
    EntityIdentifierCode,
    ReferenceIdentificationQualifier,
)
from util.address import address_segment
from util.provider import provider_segment


def billing_provider_loop(json_data: dict) -> list[str]:
    # Billing provider
    # provider (PRV) segment
    return [
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Billing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                json_data["billing"]["taxonomyCode"],
            ]
        )
        + "~",
        # name (NM1) segment
        *provider_segment(
            json_data["billing"],
            EntityIdentifierCode.BillingProvider,
            ReferenceIdentificationQualifier.NationalProviderIdentifier,
        ),
        *address_segment(json_data["billing"]["address"]),
        "*".join(
            [
                SegmentHeader.Reference.value,
                ReferenceIdentificationQualifier.EmployerIdentificationNumber.value,
                json_data["billing"]["employerId"],
            ]
        )
        + "~",
    ]
