import json
import sys

from pydantic import ValidationError

from constants import EntityIdentifierCode, ReferenceIdentificationQualifier
from models.claim import Claim
from util import (
    billing_provider_loop,
    claim_information_loop,
    entity_segment,
    service_facility_loop,
    service_line_loop,
    subscriber_loop,
)


def get_edi(claim: Claim) -> str:
    interchange_control_header = "ISA*00*          *00*          *ZZ*AV09311993     *01*030240928      *240702*1531*^*00501*415133923*0*P*>~"
    header = [
        "GS*HC*1923294*030240928*20240702*1533*415133923*X*005010X222A1~",
        "ST*837*415133923*005010X222A1~",
        "BHT*0019*00*1*20240702*1531*CH~",
        "NM1*41*2*Mattel Industries*****46*1234567890~",
        "PER*IC*Ruth Handler*TE*8458130000~",
        "NM1*40*2*AVAILITY 5010*****46*030240928~",
        "HL*1**20*1~",
    ]

    content = [
        # "HEADER",
        *header,
        # "BILLING PROVIDER LOOP",
        *billing_provider_loop(claim.billing),
        "HL*2*1*22*0~",  # Hierarchical Level
        # "SUBSCRIBER LOOP",
        *subscriber_loop(claim.subscriber, claim.claim_information),
        # "PAYER LOOP",
        *entity_segment(
            claim.receiver,
            EntityIdentifierCode.Payer,
            ReferenceIdentificationQualifier.Payer,
        ),
        # "CLAIM INFORMATION LOOP",
        *claim_information_loop(claim.claim_information),
        # "SERVICE FACILITY LOOP",
        *service_facility_loop(claim.claim_information.service_facility_location),
        # "SERVICE LINE LOOP",
        *service_line_loop(claim),
    ]

    trailer = [
        # "TRAILER",
        f"SE*{len(content)}*415133923~",
        "GE*1*415133923~",
        "IEA*1*415133923~",
    ]

    return "\n".join(
        [
            interchange_control_header,
            *content,
            *trailer,
        ]
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python json_to_edi.py <path_to_json_file>")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.lower().endswith(".json"):
        print("Error: File must have a .json extension")
        sys.exit(1)
    try:
        with open(filename) as file:
            json_data = json.load(file)
            claim = Claim.model_validate(json_data)
        print(get_edi(claim))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not valid JSON")
        sys.exit(1)
    except ValidationError as e:
        print(f"Error: JSON validation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
