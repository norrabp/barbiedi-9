from typing import Optional

from models.camel_case_base_model import CamelCaseBaseModel


class Address(CamelCaseBaseModel):
    city: str
    state: str
    address1: str
    address2: Optional[str] = None
    postal_code: str

    def __eq__(self, other: "Address") -> bool:
        return (
            self.city == other.city
            and self.state == other.state
            and self.address1 == other.address1
            and self.address2 == other.address2
            and self.postal_code == other.postal_code
        )
