from models.address import Address
from models.base import CamelCaseBaseModel


class ServiceFacilityLocation(CamelCaseBaseModel):
    npi: str
    address: Address
    phone_name: str
    phone_number: str
    organization_name: str
