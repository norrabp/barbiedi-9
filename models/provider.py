from typing import Optional

from pydantic import ValidationInfo, field_validator

from models.address import Address
from models.base import CamelCaseBaseModel
from models.contact_information import ContactInformation


class Entity(CamelCaseBaseModel):
    npi: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    organization_name: Optional[str] = None

    # @field_validator("organization_name", "last_name", "first_name")
    # @classmethod
    # def validate_name_fields(cls, value: Optional[str], info: ValidationInfo):
    #     values = info.data
    #     if not values.get("organization_name"):
    #         if not (values.get("last_name") and values.get("first_name")):
    #             raise ValueError(
    #                 "Must provide either organization_name or both first_name and last_name"
    #             )

    #     return value


class Provider(Entity):
    employer_id: str
    taxonomy_code: str
    contact_information: ContactInformation
    address: Optional[Address] = None


class Receiver(Entity):
    pass
