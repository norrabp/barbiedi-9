from constants import (
    DateTimePeriodFormatQualifier,
    DateTimeQualifier,
    EntityIdentifierCode,
    EntityTypeQualifier,
    ProviderType,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)
from models.claim import Claim
from models.service_line import ServiceLine
from util.professional_service_segment import professional_service_segment
from util.rendering_provider_segment import rendering_provider_segment


def service_line_loop(claim: Claim) -> list[str]:
    service_line_level_rendering_provider = claim.rendering is None
    service_lines = (
        []
        if service_line_level_rendering_provider
        else [*rendering_provider_segment(claim.rendering)]
    )
    for line_num, service_line in enumerate(claim.claim_information.service_lines):
        service_lines.extend(
            individual_service_line_loop(
                service_line, line_num + 1, service_line_level_rendering_provider
            )
        )

    return service_lines


def individual_service_line_loop(
    service_line: ServiceLine, line_num: int, include_rendering_provider: bool
) -> list[str]:
    service_line_segments = [
        "*".join(
            [
                SegmentHeader.ServiceLineNumber.value,
                str(line_num),
            ]
        )
        + "~",
        *professional_service_segment(service_line.professional_service),
        "*".join(
            [
                SegmentHeader.ServiceDate.value,
                DateTimeQualifier.Service.value,
                DateTimePeriodFormatQualifier.CCYYMMDD.value,
                service_line.service_date,
            ]
        )
        + "~",
    ]
    if service_line.rendering_provider and include_rendering_provider:
        service_line_segments.extend(
            rendering_provider_segment(service_line.rendering_provider)
        )
    return service_line_segments
