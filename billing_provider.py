from constants import (
    SegmentHeader,
    ProviderType,
    EntityIdentifierCode,
    ReferenceIdentificationQualifier,
)


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