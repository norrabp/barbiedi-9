import enum


class SegmentHeader(enum.Enum):
    Provider = "PRV"
    Name = "NM1"
    AddressLine1 = "N3"
    CityStatePostalCode = "N4"
    SubscriberInformation = "SBR"
    Reference = "REF"
    Demographics = "DMG"


class ProviderType(enum.Enum):
    Billing = "BI"


class RelationshipToSubscriber(enum.Enum):
    Self = "18"


class EntityIdentifierCode(enum.Enum):
    BillingProvider = "85"


class ReferenceIdentificationQualifier(enum.Enum):
    TaxonomyCode = "PXC"
    NationalProviderIdentifier = "XX"
    MemberId = "MI"
    EmployerIdentificationNumber = "EI"


class ClaimFilingIndicatorCode(enum.Enum):
    Medicaid = "MC"


class PaymentResponsibilityLevelCode(enum.Enum):
    Primary = "P"


class DateTimePeriodFormatQualifier(enum.Enum):
    CCYYMMDD = "D8"
