from constants import SegmentHeader


def professional_service_segment(json_data: dict) -> str:
    return [
        "*".join(
            [
                SegmentHeader.ServiceLine.value,
                procedure_segment(json_data),
                f"{float(json_data['professionalService']['lineItemChargeAmount']):.1f}",
                json_data["professionalService"]["measurementUnit"],
                f"{float(json_data['professionalService']['serviceUnitCount']):.1f}",
                "",
                "",
                json_data["professionalService"]["compositeDiagnosisCodePointers"][
                    "diagnosisCodePointers"
                ][0],
            ]
        )
        + "~",
    ]


def procedure_segment(json_data: dict) -> str:
    return ">".join(
        [
            json_data["professionalService"]["procedureIdentifier"],
            json_data["professionalService"]["procedureCode"],
        ]
    )