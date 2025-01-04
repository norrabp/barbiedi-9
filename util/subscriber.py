from constants import (
    ClaimFilingIndicatorCode,
    DateTimePeriodFormatQualifier,
    EntityIdentifierCode,
    EntityTypeQualifier,
    PaymentResponsibilityLevelCode,
    ReferenceIdentificationQualifier,
    RelationshipToSubscriber,
    SegmentHeader,
)
from models.claim_information import ClaimInformation
from models.patient import Patient
from util.address_segment import address_segment


def subscriber_loop(
    subscriber: Patient, claim_information: ClaimInformation
) -> list[str]:
    return [
        "*".join(
            [
                SegmentHeader.SubscriberInformation.value,
                PaymentResponsibilityLevelCode(
                    subscriber.payment_responsibility_level_code
                ).value,
                RelationshipToSubscriber.Self.value,
                "",
                "",
                "",
                "",
                "",
                "",
                ClaimFilingIndicatorCode(claim_information.claim_filing_code).value,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Name.value,
                EntityIdentifierCode.InsuredOrSubscriber.value,
                EntityTypeQualifier.Person.value,
                subscriber.last_name,
                subscriber.first_name,
                "",
                "",
                "",
                ReferenceIdentificationQualifier.MemberId.value,
                subscriber.member_id,
            ]
        )
        + "~",
        *address_segment(subscriber.address),
        "*".join(
            [
                SegmentHeader.Demographics.value,
                DateTimePeriodFormatQualifier.CCYYMMDD.value,
                subscriber.date_of_birth,
                subscriber.gender,
            ]
        )
        + "~",
    ]
