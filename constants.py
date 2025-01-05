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
    ContactInformation = "PER"
    HierarchicalLevels = "HL"
    Patient = "PAT"


class EntityIdentifierCode(str, enum.Enum):
    BillingProvider = "85"
    InsuredOrSubscriber = "IL"
    Payer = "PR"
    ServiceFacility = "77"
    RenderingProvider = "82"
    Submitter = "41"
    Patient = "QC"
    Receiver = "40"
    OrderingPhysician = "DK"
    ReferringProvider = "DN"
    PayToProvider = "87"


class ReferenceIdentificationQualifier(str, enum.Enum):
    TaxonomyCode = "PXC"
    NationalProviderIdentifier = "XX"
    MemberId = "MI"
    EmployerIdentificationNumber = "EI"
    Payer = "PI"
    PriorAuthorizationNumber = "G1"
    ETIN = "46"
    DunAndBradstreet = "01"
    MutuallyDefined = "ZZ"
    ClaimOfficeNumber = "FY"
    ProviderCommercialNumber = "G2"
    OriginalReferenceNumber = "F8"
    SocialSecurityNumber = "SY"
    TaxIdentificationNumber = "TJ"


class ProviderType(str, enum.Enum):
    Billing = "BI"
    Performing = "PE"


class RelationshipToSubscriber(str, enum.Enum):
    Spouse = "01"
    BiologicalChild = "02"
    Parent = "03"
    Sibling = "14"
    Self = "18"
    Child = "19"
    Employee = "20"
    SponsoredDependent = "23"
    Guardian = "26"
    SignificantOther = "29"


class DateTimePeriodFormatQualifier(str, enum.Enum):
    YYYYMMDD = "D8"
    YYMMDD = "D6"


class ClaimFilingIndicatorCode(str, enum.Enum):
    Medicaid = "MC"
    BlueCrossBlueShield = "BL"
    CommercialInsuranceCompany = "CI"
    SupplementalClaim = "05"
    InitialClaim = "08"
    SelfPay = "09"
    PreferredProviderOrganization = "12"
    ExclusiveProviderOrganization = "14"
    MedicarePartA = "MA"
    MedicarePartB = "MB"
    VeteranAffairsPlan = "VA"


class PaymentResponsibilityLevelCode(str, enum.Enum):
    Primary = "P"
    Secondary = "S"
    Tertiary = "T"
    Unknown = "U"


class DateTimeQualifier(str, enum.Enum):
    Service = "472"


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
    Unknown = "X"


class ProviderSignatureIndicator(str, enum.Enum):
    Yes = "Y"
    No = "N"


class BenefitsAssignmentCertificationIndicator(str, enum.Enum):
    Yes = "Y"
    No = "N"
    NotApplicable = "W"


class ReleaseOfInformationCode(str, enum.Enum):
    InformedConsent = "I"
    ReleaseForClaim = "Y"


class PlanParticipationCode(str, enum.Enum):
    # Should update with more values when they come in
    Assigned = "A"
    ClinicalLabServicesOnly = "B"
    NotAssigned = "C"


class PlaceOfServiceCode(str, enum.Enum):
    TelehealthNotAtHome = "02"
    School = "03"
    TelehealthPatientHome = "10"
    Office = "11"
    Home = "12"
    NursingFacility = "32"


class DiagnosisTypeCode(str, enum.Enum):
    Principal = "ABK"
    Clinical = "ABF"


class ClaimFrequencyCode(str, enum.Enum):
    Original = "1"
    Subsequent = "7"
    Replacement = "8"
    Void = "9"


class MeasurementUnit(str, enum.Enum):
    Unit = "UN"
    Minutes = "MJ"


class ContactFunctionCode(str, enum.Enum):
    InformationContact = "IC"


class CommunicationNumberQualifier(str, enum.Enum):
    Telephone = "TE"
    Fax = "FX"
    Email = "EM"


class HierarchicalLevelCode(str, enum.Enum):
    InformationSource = "20"
    Subscriber = "22"
    Patient = "23"
