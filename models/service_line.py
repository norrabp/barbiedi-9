from typing import List, Optional

from constants import MeasurementUnit
from models.base import CamelCaseBaseModel
from models.provider import Provider


class CompositeDiagnosisCodePointers(CamelCaseBaseModel):
    diagnosis_code_pointers: List[str]


class ProfessionalService(CamelCaseBaseModel):
    procedure_code: str
    measurement_unit: MeasurementUnit
    service_unit_count: float
    procedure_identifier: str
    line_item_charge_amount: float
    composite_diagnosis_code_pointers: CompositeDiagnosisCodePointers


class ServiceLine(CamelCaseBaseModel):
    service_date: str
    rendering_provider: Optional[Provider] = None
    professional_service: ProfessionalService
    provider_control_number: str
