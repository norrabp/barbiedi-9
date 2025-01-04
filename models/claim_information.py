from typing import List

from constants import (
    ClaimFilingIndicatorCode,
    ClaimFrequencyCode,
    DiagnosisCode,
    DiagnosisTypeCode,
    PlaceOfServiceCode,
    PlanParticipationCode,
    YesNo,
)
from models.base import CamelCaseBaseModel
from models.service_facility_location import ServiceFacilityLocation
from models.service_line import ServiceLine


class HealthCareCode(CamelCaseBaseModel):
    diagnosis_code: DiagnosisCode
    diagnosis_type_code: DiagnosisTypeCode


class ClaimSupplementalInformation(CamelCaseBaseModel):
    prior_authorization_number: str


class ClaimInformation(CamelCaseBaseModel):
    service_lines: List[ServiceLine]
    claim_filing_code: ClaimFilingIndicatorCode
    claim_charge_amount: float
    claim_frequency_code: ClaimFrequencyCode
    place_of_service_code: PlaceOfServiceCode
    signature_indicator: YesNo
    patient_control_number: str
    plan_participation_code: PlanParticipationCode
    release_information_code: YesNo
    service_facility_location: ServiceFacilityLocation
    health_care_code_information: List[HealthCareCode]
    claim_supplemental_information: ClaimSupplementalInformation
    benefits_assignment_certification_indicator: YesNo
