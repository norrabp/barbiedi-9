from constants import (DateTimePeriodFormatQualifier, DateTimeQualifier,
                       EntityIdentifierCode, ProviderType,
                       ReferenceIdentificationQualifier, SegmentHeader)
from edi.entity_segment import entity_segment
from models.entity import Provider


def rendering_provider_segment(provider: Provider) -> str:
    return [
        *entity_segment(
            provider,
            EntityIdentifierCode.RenderingProvider,  # 82
            ReferenceIdentificationQualifier.NationalProviderIdentifier,  # XX
        ),
        "*".join(
            [
                SegmentHeader.Provider,  # PRV
                ProviderType.Performing,  # PE
                ReferenceIdentificationQualifier.TaxonomyCode,  # PXC
                provider.taxonomy_code,
            ]
        )
        + "~",
    ]
