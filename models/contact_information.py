from models.base import CamelCaseBaseModel
from typing import Optional


class ContactInformation(CamelCaseBaseModel):
    name: str
    phone_number: Optional[str] = None
