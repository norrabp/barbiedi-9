from constants import SegmentHeader
from models.service_line import ProfessionalService


def professional_service_segment(professional_service: ProfessionalService) -> str:
    return [
        "*".join(
            [
                SegmentHeader.ServiceLine.value,
                procedure_segment(professional_service),
                f"{professional_service.line_item_charge_amount:.1f}",
                professional_service.measurement_unit,
                f"{professional_service.service_unit_count:.1f}",
                "",
                "",
                professional_service.composite_diagnosis_code_pointers.diagnosis_code_pointers[
                    0
                ],
            ]
        )
        + "~",
    ]


def procedure_segment(professional_service: ProfessionalService) -> str:
    return ">".join(
        [
            professional_service.procedure_identifier,
            professional_service.procedure_code,
        ]
    )
