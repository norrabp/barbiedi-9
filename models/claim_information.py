from typing import List

from constants import (
    BenefitsAssignmentCertificationIndicator,
    ClaimFilingIndicatorCode,
    ClaimFrequencyCode,
    DiagnosisTypeCode,
    PlaceOfServiceCode,
    PlanParticipationCode,
    ProviderSignatureIndicator,
    ReleaseOfInformationCode,
)
from models.camel_case_base_model import CamelCaseBaseModel
from models.entity import ServiceFacilityLocation
from models.service_line import ServiceLine


class HealthCareCode(CamelCaseBaseModel):
    diagnosis_code: str
    diagnosis_type_code: DiagnosisTypeCode


class ClaimSupplementalInformation(CamelCaseBaseModel):
    prior_authorization_number: str


class ClaimInformation(CamelCaseBaseModel):
    service_lines: List[ServiceLine]
    claim_filing_code: ClaimFilingIndicatorCode
    claim_charge_amount: float
    claim_frequency_code: ClaimFrequencyCode
    place_of_service_code: PlaceOfServiceCode
    signature_indicator: ProviderSignatureIndicator
    patient_control_number: str
    plan_participation_code: PlanParticipationCode
    release_information_code: ReleaseOfInformationCode
    service_facility_location: ServiceFacilityLocation
    health_care_code_information: List[HealthCareCode]
    claim_supplemental_information: ClaimSupplementalInformation
    benefits_assignment_certification_indicator: (
        BenefitsAssignmentCertificationIndicator
    )
