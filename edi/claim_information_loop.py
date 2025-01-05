from constants import (FacilityCodeQualifier, ReferenceIdentificationQualifier,
                       SegmentHeader)
from models.claim_information import ClaimInformation, HealthCareCode


def claim_information_loop(claim_information: ClaimInformation) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.ClaimInformation,  # CLM
                claim_information.patient_control_number,
                f"{claim_information.claim_charge_amount:.1f}",
                "",
                "",
                service_facility_segment(claim_information),
                claim_information.signature_indicator,
                claim_information.plan_participation_code,
                claim_information.benefits_assignment_certification_indicator,
                claim_information.release_information_code,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Reference,  # REF
                ReferenceIdentificationQualifier.PriorAuthorizationNumber,  # G1
                claim_information.claim_supplemental_information.prior_authorization_number,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.HealthCareDiagnosisCode,  # HI
                diagnosis_code_segment(
                    claim_information.health_care_code_information[0]
                ),
            ]
        )
        + "~",
    ]


def service_facility_segment(claim_information: ClaimInformation) -> str:
    return ">".join(
        [
            claim_information.place_of_service_code,
            FacilityCodeQualifier.ProfessionalOrDentalServices,  # B
            claim_information.claim_frequency_code,
        ]
    )


def diagnosis_code_segment(health_care_code: HealthCareCode) -> str:
    return ">".join(
        [
            health_care_code.diagnosis_type_code,
            health_care_code.diagnosis_code,
        ]
    )
