import enum


class SegmentHeader(enum.Enum):
    Provider = "PRV"
    Name = "NM1"
    AddressLine1 = "N3"
    CityStatePostalCode = "N4"
    SubscriberInformation = "SBR"
    Reference = "REF"
    Demographics = "DMG"
    ClaimInformation = "CLM"
    HealthCareDiagnosisCode = "HI"
    ServiceLineNumber = "LX"
    ServiceLine = "SV1"
    ServiceDate = "DTP"
    RenderingProvider = "PRV"


class ProviderType(enum.Enum):
    Billing = "BI"
    Performing = "PE"


class RelationshipToSubscriber(enum.Enum):
    Self = "18"


class EntityIdentifierCode(enum.Enum):
    BillingProvider = "85"
    InsuredOrSubscriber = "IL"
    Payer = "PR"
    ServiceFacility = "77"
    RenderingProvider = "82"


class ReferenceIdentificationQualifier(enum.Enum):
    TaxonomyCode = "PXC"
    NationalProviderIdentifier = "XX"
    MemberId = "MI"
    EmployerIdentificationNumber = "EI"
    Payer = "PI"
    PriorAuthorizationNumber = "G1"


class ClaimFilingIndicatorCode(enum.Enum):
    Medicaid = "MC"
    BlueCrossBlueShield = "BL"


class PaymentResponsibilityLevelCode(enum.Enum):
    Primary = "P"


class DateTimeQualifier(enum.Enum):
    Service = "472"


class DateTimePeriodFormatQualifier(enum.Enum):
    CCYYMMDD = "D8"


class EntityTypeQualifier(enum.Enum):
    Person = "1"
    NonPerson = "2"


class PayerIdentifier(enum.Enum):
    WIMCD = "WIMCD"


class FacilityCodeQualifier(enum.Enum):
    ProfessionalOrDentalServices = "B"


class ProductOrServiceQualifier(enum.Enum):
    HCPCS = "HC"
