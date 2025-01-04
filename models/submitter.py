from models.base import CamelCaseBaseModel
from models.contact_information import ContactInformation


class Submitter(CamelCaseBaseModel):
    organization_name: str
    contact_information: ContactInformation
