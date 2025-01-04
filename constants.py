import enum


class SegmentHeader(str, enum.Enum):
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


class ProviderType(str, enum.Enum):
    Billing = "BI"
    Performing = "PE"


class RelationshipToSubscriber(str, enum.Enum):
    Self = "18"


class EntityIdentifierCode(str, enum.Enum):
    BillingProvider = "85"
    InsuredOrSubscriber = "IL"
    Payer = "PR"
    ServiceFacility = "77"
    RenderingProvider = "82"


class ReferenceIdentificationQualifier(str, enum.Enum):
    TaxonomyCode = "PXC"
    NationalProviderIdentifier = "XX"
    MemberId = "MI"
    EmployerIdentificationNumber = "EI"
    Payer = "PI"
    PriorAuthorizationNumber = "G1"


class ClaimFilingIndicatorCode(str, enum.Enum):
    # Should update with more values when they come in
    Medicaid = "MC"
    BlueCrossBlueShield = "BL"
    CommercialInsuranceCompany = "CI"


class PaymentResponsibilityLevelCode(str, enum.Enum):
    Patient = "P"


class DateTimeQualifier(str, enum.Enum):
    Service = "472"


class DateTimePeriodFormatQualifier(str, enum.Enum):
    CCYYMMDD = "D8"


class EntityTypeQualifier(str, enum.Enum):
    Person = "1"
    NonPerson = "2"


class PayerIdentifier(str, enum.Enum):
    WIMCD = "WIMCD"


class FacilityCodeQualifier(str, enum.Enum):
    ProfessionalOrDentalServices = "B"


class ProductOrServiceQualifier(str, enum.Enum):
    HCPCS = "HC"


class Gender(str, enum.Enum):
    Male = "M"
    Female = "F"
    Other = "O"


class YesNo(str, enum.Enum):
    Yes = "Y"
    No = "N"


class PlanParticipationCode(str, enum.Enum):
    # Should update with more values when they come in
    Active = "A"


class PlaceOfServiceCode(str, enum.Enum):
    # Should update with more values when they come in
    Office = "11"
    Home = "12"


class DiagnosisTypeCode(str, enum.Enum):
    ICD10CM = "ABK"


class ClaimFrequencyCode(str, enum.Enum):
    # Should update with more values when they come in
    Original = "1"


class DiagnosisCode(str, enum.Enum):
    # Should update with more values when they come in
    F840 = "F840"


class MeasurementUnit(str, enum.Enum):
    Unit = "UN"
