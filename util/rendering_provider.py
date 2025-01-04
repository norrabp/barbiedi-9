from constants import (
    DateTimeQualifier,
    DateTimePeriodFormatQualifier,
    EntityIdentifierCode,
    ReferenceIdentificationQualifier,
    SegmentHeader,
    ProviderType,
)
from util.provider import provider_segment


def rendering_provider_segment(json_data: dict) -> str:
    return [
        *provider_segment(
            json_data,
            EntityIdentifierCode.RenderingProvider,
            ReferenceIdentificationQualifier.NationalProviderIdentifier,
        ),
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Performing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                json_data["taxonomyCode"],
            ]
        )
        + "~",
    ]