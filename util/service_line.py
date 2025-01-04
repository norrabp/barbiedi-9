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
    service_lines = []
    for line_num, service_line_json_data in enumerate(
        json_data["claimInformation"]["serviceLines"]
    ):
        service_lines.extend(
            individual_service_line_loop(service_line_json_data, line_num + 1)
        )

    return service_lines


def individual_service_line_loop(json_data: dict, line_num: int) -> list[str]:
    service_line_segments = [
        "*".join(
            [
                SegmentHeader.ServiceLineNumber.value,
                str(line_num),
            ]
        )
        + "~",
        *professional_service_segment(json_data)
    ]
    if "renderingProvider" in json_data:
        service_line_segments.extend(rendering_provider_segment(json_data))
    return service_line_segments


