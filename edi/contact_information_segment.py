from constants import (CommunicationNumberQualifier, ContactFunctionCode,
                       SegmentHeader)
from models.contact_information import ContactInformation


def contact_information_segment(contact_information: ContactInformation) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.ContactInformation,  # PER
                ContactFunctionCode.InformationContact,  # IC
                contact_information.name,
                CommunicationNumberQualifier.Telephone,  # TE
                contact_information.phone_number,
            ]
        )
        + "~"
    ]
