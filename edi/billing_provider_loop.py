from constants import (EntityIdentifierCode, EntityTypeQualifier, ProviderType,
                       ReferenceIdentificationQualifier, SegmentHeader)
from edi.address_segment import address_segment
from edi.contact_information_segment import contact_information_segment
from edi.entity_segment import entity_segment
from models.claim import Claim
from models.entity import Provider


def billing_provider_loop(claim: Claim) -> list[str]:
    # Billing provider
    # provider (PRV) segment
    content = [
        "*".join(
            [
                SegmentHeader.Provider,  # PRV
                ProviderType.Billing,  # BI
                ReferenceIdentificationQualifier.TaxonomyCode,  # PXC
                claim.billing.taxonomy_code,
            ]
        )
        + "~",
        # name (NM1) segment
        *entity_segment(
            claim.billing,
            EntityIdentifierCode.BillingProvider,  # 85
            ReferenceIdentificationQualifier.NationalProviderIdentifier,  # XX
        ),
        *address_segment(claim.billing.address),
        "*".join(
            [
                SegmentHeader.Reference,  # REF
                ReferenceIdentificationQualifier.EmployerIdentificationNumber,  # EI
                claim.billing.employer_id,
            ]
        )
        + "~",
    ]
    if claim.billing.contact_information != claim.submitter.contact_information:
        # Only add billing contact information if it's different from the submitter
        content.append(*contact_information_segment(claim.billing.contact_information))
    return content
