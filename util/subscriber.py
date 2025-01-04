from constants import (
    DateTimePeriodFormatQualifier,
    EntityIdentifierCode,
    EntityTypeQualifier,
    SegmentHeader,
    RelationshipToSubscriber,
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
                ClaimFilingIndicatorCode(
                    json_data["claimInformation"]["claimFilingCode"]
                ).value,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Name.value,
                EntityIdentifierCode.InsuredOrSubscriber.value,
                EntityTypeQualifier.Person.value,
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
        "*".join(
            [
                SegmentHeader.Demographics.value,
                DateTimePeriodFormatQualifier.CCYYMMDD.value,
                json_data["subscriber"]["dateOfBirth"],
                json_data["subscriber"]["gender"],
            ]
        )
        + "~",
    ]
