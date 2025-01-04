from constants import (
    FacilityCodeQualifier,
    ReferenceIdentificationQualifier,
    SegmentHeader,
)


def claim_information_loop(json_data: dict) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.ClaimInformation.value,
                json_data["claimInformation"]["patientControlNumber"],
                f"{float(json_data['claimInformation']['claimChargeAmount']):.1f}",
                "",
                "",
                service_facility_segment(json_data["claimInformation"]),
                json_data["claimInformation"]["signatureIndicator"],
                json_data["claimInformation"]["planParticipationCode"],
                json_data["claimInformation"][
                    "benefitsAssignmentCertificationIndicator"
                ],
                json_data["claimInformation"]["releaseInformationCode"],
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Reference.value,
                ReferenceIdentificationQualifier.PriorAuthorizationNumber.value,
                json_data["claimInformation"]["claimSupplementalInformation"][
                    "priorAuthorizationNumber"
                ],
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.HealthCareDiagnosisCode.value,
                diagnosis_code_segment(
                    json_data["claimInformation"]["healthCareCodeInformation"][0]
                ),
            ]
        )
        + "~",
    ]


def service_facility_segment(json_data: dict) -> str:
    return ">".join(
        [
            json_data["placeOfServiceCode"],
            FacilityCodeQualifier.ProfessionalOrDentalServices.value,
            json_data["claimFrequencyCode"],
        ]
    )


def diagnosis_code_segment(json_data: dict) -> str:
    return ">".join(
        [
            json_data["diagnosisTypeCode"],
            json_data["diagnosisCode"],
        ]
    )
