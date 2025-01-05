from typing import Optional

from models.camel_case_base_model import CamelCaseBaseModel
from models.claim_information import ClaimInformation
from models.entity import Provider, Receiver, Submitter
from models.patient import Patient


class Claim(CamelCaseBaseModel):
    billing: Provider
    ordering: Optional[Provider] = None
    receiver: Receiver
    submitter: Submitter
    dependent: Optional[Patient] = None
    rendering: Optional[Provider] = None
    subscriber: Patient
    control_number: str
    claim_information: ClaimInformation
