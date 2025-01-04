from typing import Optional

from models.base import CamelCaseBaseModel


class Address(CamelCaseBaseModel):
    city: str
    state: str
    address1: str
    address2: Optional[str] = None
    postal_code: str
