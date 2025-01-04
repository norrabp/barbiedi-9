from constants import (
    DateTimePeriodFormatQualifier,
    DateTimeQualifier,
    EntityIdentifierCode,
    EntityTypeQualifier,
    ProviderType,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from util.professional_service import professional_service_segment
from util.rendering_provider import rendering_provider_segment


def service_line_loop(json_data: dict) -> list[str]:
    service_line_level_rendering_provider = "rendering" not in json_data
    service_lines = [] if service_line_level_rendering_provider else [*rendering_provider_segment(json_data["rendering"])]
    for line_num, service_line_json_data in enumerate(
        json_data["claimInformation"]["serviceLines"]
    ):
        service_lines.extend(
            individual_service_line_loop(service_line_json_data, line_num + 1, service_line_level_rendering_provider)
        )

    return service_lines


def individual_service_line_loop(json_data: dict, line_num: int, include_rendering_provider: bool) -> list[str]:
    service_line_segments = [
        "*".join(
            [
                SegmentHeader.ServiceLineNumber.value,
                str(line_num),
            ]
        )
        + "~",
        *professional_service_segment(json_data),
        "*".join(
            [
                SegmentHeader.ServiceDate.value,
                DateTimeQualifier.Service.value,
                DateTimePeriodFormatQualifier.CCYYMMDD.value,
                json_data["serviceDate"],
            ]
        )
        + "~",
    ]
    if "renderingProvider" in json_data and include_rendering_provider:
        service_line_segments.extend(rendering_provider_segment(json_data["renderingProvider"]))
    return service_line_segments


