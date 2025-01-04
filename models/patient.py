from typing import Optional

from constants import Gender, PaymentResponsibilityLevelCode
from models.address import Address
from models.base import CamelCaseBaseModel


class Patient(CamelCaseBaseModel):
    address: Address
    last_name: str
    member_id: str
    first_name: str
    date_of_birth: str
    group_number: Optional[str] = None
    payment_responsibility_level_code: PaymentResponsibilityLevelCode
    gender: Optional[Gender] = None
