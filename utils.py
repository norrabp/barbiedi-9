from constants import (
    SegmentHeader,
    ProviderType,
    RelationshipToSubscriber,
    EntityIdentifierCode,
    ReferenceIdentificationQualifier,
    ClaimFilingIndicatorCode,
    PaymentResponsibilityLevelCode,
)


def subscriber_loop(json_data: dict) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.SubscriberInformation.value,
                PaymentResponsibilityLevelCode(
                    json_data["subscriber"]["paymentResponsibilityLevelCode"]
                ).value,
                RelationshipToSubscriber.Self.value,
                "",
                "",
                "",
                "",
                "",
                "",
                ClaimFilingIndicatorCode.Medicaid.value,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Name.value,
                "IL",
                "1",
                json_data["subscriber"]["lastName"],
                json_data["subscriber"]["firstName"],
                "",
                "",
                "",
                ReferenceIdentificationQualifier.MemberId.value,
                json_data["subscriber"]["memberId"],
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.AddressLine1.value,
                json_data["subscriber"]["address"]["address1"],
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.CityStatePostalCode.value,
                json_data["subscriber"]["address"]["city"],
                json_data["subscriber"]["address"]["state"],
                json_data["subscriber"]["address"]["postalCode"],
            ]
        )
        + "~",
    ]


def billing_provider_loop(json_data: dict) -> list[str]:
    # Billing provider
    # provider (PRV) segment
    return [
        "*".join(
            [
                SegmentHeader.Provider.value,
                ProviderType.Billing.value,
                ReferenceIdentificationQualifier.TaxonomyCode.value,
                json_data["billing"]["taxonomyCode"],
            ]
        )
        + "~",
        # name (NM1) segment
        "*".join(
            [
                SegmentHeader.Name.value,
                EntityIdentifierCode.BillingProvider.value,
                *(["2"] if "organizationName" in json_data["billing"] else ["1"]),
                json_data["billing"]["organizationName"],
                "",
                "",
                "",
                "",
                ReferenceIdentificationQualifier.NationalProviderIdentifier.value,
                json_data["billing"]["npi"],
            ]
        )
        + "~",
        # address line 1 (N3) segment
        "*".join(
            [
                SegmentHeader.AddressLine1.value,
                json_data["billing"]["address"]["address1"],
            ]
        )
        + "~",
        # city, state, postal code (N4) segment
        "*".join(
            [
                SegmentHeader.CityStatePostalCode.value,
                json_data["billing"]["address"]["city"],
                json_data["billing"]["address"]["state"],
                json_data["billing"]["address"]["postalCode"],
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Reference.value,
                ReferenceIdentificationQualifier.EmployerIdentificationNumber.value,
                json_data["billing"]["employerId"],
            ]
        )
        + "~",
    ]