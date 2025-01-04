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
        "*".join(
            [
                SegmentHeader.ServiceDate.value,
                DateTimeQualifier.Service.value,
                DateTimePeriodFormatQualifier.CCYYMMDD.value,
                json_data["serviceDate"],
            ]
        )
        + "~",
        *provider_segment(
            json_data["renderingProvider"],
            EntityIdentifierCode.RenderingProvider,
            ReferenceIdentificationQualifier.NationalProviderIdentifier,
        ),
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Performing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                json_data["renderingProvider"]["taxonomyCode"],
            ]
        )
        + "~",
    ]