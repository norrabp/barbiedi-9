from constants import SegmentHeader
from models.address import Address


def address_segment(address: Address) -> str:
    line_one_content = [
        SegmentHeader.AddressLine1,  # N3
        address.address1,
    ]
    if address.address2:
        line_one_content.append(address.address2)
    return [
        # address line 1 (N3) segment
        "*".join(line_one_content) + "~",
        # city, state, postal code (N4) segment
        "*".join(
            [
                SegmentHeader.CityStatePostalCode,  # N4
                address.city,
                address.state,
                address.postal_code,
            ]
        )
        + "~",
    ]
