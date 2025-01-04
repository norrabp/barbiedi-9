from constants import (
    EntityIdentifierCode,
    EntityTypeQualifier,
    ProviderType,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from models.provider import Provider
from util.address_segment import address_segment
from util.entity_segment import entity_segment


def billing_provider_loop(provider: Provider) -> list[str]:
    # Billing provider
    # provider (PRV) segment
    return [
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Billing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                provider.taxonomy_code,
            ]
        )
        + "~",
        # name (NM1) segment
        *entity_segment(
            provider,
            EntityIdentifierCode.BillingProvider,
            ReferenceIdentificationQualifier.NationalProviderIdentifier,
        ),
        *address_segment(provider.address),
        "*".join(
            [
                SegmentHeader.Reference.value,
                ReferenceIdentificationQualifier.EmployerIdentificationNumber.value,
                provider.employer_id,
            ]
        )
        + "~",
    ]
