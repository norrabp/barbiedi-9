from constants import (ClaimFilingIndicatorCode, DateTimePeriodFormatQualifier,
                       EntityIdentifierCode, EntityTypeQualifier,
                       PaymentResponsibilityLevelCode,
                       ReferenceIdentificationQualifier,
                       RelationshipToSubscriber, SegmentHeader)
from edi.address_segment import address_segment
from models.claim import Claim
from models.claim_information import ClaimInformation
from models.patient import Patient


def subscriber_loop(
    claim: Claim,
) -> list[str]:
    content = [
        "*".join(
            [
                SegmentHeader.SubscriberInformation,  # SBR
                claim.subscriber.payment_responsibility_level_code,
                RelationshipToSubscriber.Self if not claim.dependent else "",  # 18
                "",
                "",
                "",
                "",
                "",
                "",
                claim.claim_information.claim_filing_code,
            ]
        )
        + "~",
        "*".join(
            [
                SegmentHeader.Name,  # NM1
                EntityIdentifierCode.InsuredOrSubscriber,  # IL
                EntityTypeQualifier.Person,  # 1
                claim.subscriber.last_name,
                claim.subscriber.first_name,
                "",
                "",
                "",
                ReferenceIdentificationQualifier.MemberId,  # MI
                claim.subscriber.member_id,
            ]
        )
        + "~",
    ]
    if not claim.dependent:
        # This info is shown for the dependent instead of the subscriber
        content.extend(
            [
                *address_segment(claim.subscriber.address),
                "*".join(
                    [
                        SegmentHeader.Demographics,  # DMG
                        DateTimePeriodFormatQualifier.YYYYMMDD,  # D8
                        claim.subscriber.date_of_birth,
                        (claim.subscriber.gender if claim.subscriber.gender else ""),
                    ]
                )
                + "~",
            ]
        )
    return content
