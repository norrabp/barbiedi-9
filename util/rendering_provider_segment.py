from constants import (
    DateTimePeriodFormatQualifier,
    DateTimeQualifier,
    EntityIdentifierCode,
    ProviderType,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from models.provider import Provider
from util.entity_segment import entity_segment


def rendering_provider_segment(provider: Provider) -> str:
    return [
        *entity_segment(
            provider,
            EntityIdentifierCode.RenderingProvider,
            ReferenceIdentificationQualifier.NationalProviderIdentifier,
        ),
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Performing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                provider.taxonomy_code,
            ]
        )
        + "~",
    ]
