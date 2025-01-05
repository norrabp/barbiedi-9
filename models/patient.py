from typing import Optional

from constants import Gender, PaymentResponsibilityLevelCode, RelationshipToSubscriber
from models.address import Address
from models.camel_case_base_model import CamelCaseBaseModel


class Patient(CamelCaseBaseModel):
    address: Address
    last_name: str
    member_id: str
    first_name: str
    date_of_birth: str
    group_number: Optional[str] = None
    payment_responsibility_level_code: PaymentResponsibilityLevelCode
    gender: Optional[Gender] = None
    relationship_to_subscriber_code: Optional[RelationshipToSubscriber] = None
