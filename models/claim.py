from typing import Optional

from models.base import CamelCaseBaseModel
from models.claim_information import ClaimInformation
from models.patient import Patient
from models.provider import Provider, Receiver
from models.submitter import Submitter


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
