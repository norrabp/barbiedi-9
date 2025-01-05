import json
import sys

from pydantic import ValidationError

from constants import EntityIdentifierCode, ReferenceIdentificationQualifier
from edi.billing_provider_loop import billing_provider_loop
from edi.claim_information_loop import claim_information_loop
from edi.dependent_loop import dependent_loop
from edi.entity_segment import entity_segment
from edi.service_facility_segment import service_facility_segment
from edi.service_line_segment import service_line_segment
from edi.subscriber_loop import subscriber_loop
from models.claim import Claim
from util.get_hierarchical_levels import get_hierarchical_levels


def get_edi(claim: Claim) -> str:
    """
    Generate an EDI 837 claim from a JSON claim.
    """
    interchange_control_header = "ISA*00*          *00*          *ZZ*AV09311993     *01*030240928      *240702*1531*^*00501*415133923*0*P*>~"
    header = [
        "GS*HC*1923294*030240928*20240702*1533*415133923*X*005010X222A1~",
        "ST*837*415133923*005010X222A1~",
        "BHT*0019*00*1*20240702*1531*CH~",
        "NM1*41*2*Mattel Industries*****46*1234567890~",
        "PER*IC*Ruth Handler*TE*8458130000~",
        "NM1*40*2*AVAILITY 5010*****46*030240928~",
    ]

    hierarchical_levels = get_hierarchical_levels(claim)

    content = [
        # "HEADER",
        *header,
        hierarchical_levels[0],
        # "BILLING PROVIDER LOOP",
        *billing_provider_loop(claim),
        # "SUBSCRIBER LOOP",
        hierarchical_levels[1],
        *subscriber_loop(claim),
        # "PAYER LOOP",
        *entity_segment(
            claim.receiver,
            EntityIdentifierCode.Payer,
            ReferenceIdentificationQualifier.Payer,
        ),
        # "DEPENDENT LOOP",
        *dependent_loop(claim.dependent, hierarchical_levels),
        # "CLAIM INFORMATION LOOP",
        *claim_information_loop(claim.claim_information),
        # "SERVICE FACILITY LOOP",
        *service_facility_segment(claim),
        # "SERVICE LINE LOOP",
        *service_line_segment(claim),
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
        # In a production environment, this would be a great way to detect
        # changes in json claim schema or scenarios we failed to account for.
        # We could store unprocessed claims to either be manually processed later
        # or to be processed ad-hoc once the appropriate changes are made to
        # this library
        print(f"Error: JSON validation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
