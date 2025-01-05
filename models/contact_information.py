from typing import Optional

from models.camel_case_base_model import CamelCaseBaseModel


class ContactInformation(CamelCaseBaseModel):
    name: str
    phone_number: Optional[str] = None

    def __eq__(self, other: "ContactInformation") -> bool:
        return self.name == other.name and self.phone_number == other.phone_number
