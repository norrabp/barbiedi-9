from typing import Optional

from pydantic import ValidationInfo, field_validator

from models.address import Address
from models.camel_case_base_model import CamelCaseBaseModel
from models.contact_information import ContactInformation


class Entity(CamelCaseBaseModel):
    # TODO: Add validation that either organization_name or first_name and last_name are provided
    npi: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    organization_name: Optional[str] = None


class Provider(Entity):
    employer_id: str
    taxonomy_code: str
    contact_information: ContactInformation
    address: Optional[Address] = None


class Receiver(Entity):
    pass


class Submitter(Entity):
    contact_information: ContactInformation


class ServiceFacilityLocation(Entity):
    address: Address
    phone_name: str
    phone_number: str
