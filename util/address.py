

from constants import SegmentHeader


def address_segment(json_data: dict) -> str:
    line_one_content = [
        SegmentHeader.AddressLine1.value,
        json_data["address1"],
    ]
    if "address2" in json_data:
        line_one_content.append(json_data["address2"])
    return [
        # address line 1 (N3) segment
        "*".join(line_one_content)
        + "~",
        # city, state, postal code (N4) segment
        "*".join(
            [
                SegmentHeader.CityStatePostalCode.value,
                json_data["city"],
                json_data["state"],
                json_data["postalCode"],
            ]
        )
        + "~",
    ]