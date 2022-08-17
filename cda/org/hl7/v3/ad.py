from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.adxp_additional_locator import AdxpAdditionalLocator
from cda.org.hl7.v3.adxp_building_number_suffix import AdxpBuildingNumberSuffix
from cda.org.hl7.v3.adxp_care_of import AdxpCareOf
from cda.org.hl7.v3.adxp_census_tract import AdxpCensusTract
from cda.org.hl7.v3.adxp_city import AdxpCity
from cda.org.hl7.v3.adxp_country import AdxpCountry
from cda.org.hl7.v3.adxp_county import AdxpCounty
from cda.org.hl7.v3.adxp_delimiter import AdxpDelimiter
from cda.org.hl7.v3.adxp_delivery_address_line import AdxpDeliveryAddressLine
from cda.org.hl7.v3.adxp_delivery_installation_area import AdxpDeliveryInstallationArea
from cda.org.hl7.v3.adxp_delivery_installation_qualifier import AdxpDeliveryInstallationQualifier
from cda.org.hl7.v3.adxp_delivery_installation_type import AdxpDeliveryInstallationType
from cda.org.hl7.v3.adxp_delivery_mode import AdxpDeliveryMode
from cda.org.hl7.v3.adxp_delivery_mode_identifier import AdxpDeliveryModeIdentifier
from cda.org.hl7.v3.adxp_direction import AdxpDirection
from cda.org.hl7.v3.adxp_house_number import AdxpHouseNumber
from cda.org.hl7.v3.adxp_house_number_numeric import AdxpHouseNumberNumeric
from cda.org.hl7.v3.adxp_post_box import AdxpPostBox
from cda.org.hl7.v3.adxp_postal_code import AdxpPostalCode
from cda.org.hl7.v3.adxp_precinct import AdxpPrecinct
from cda.org.hl7.v3.adxp_state import AdxpState
from cda.org.hl7.v3.adxp_street_address_line import AdxpStreetAddressLine
from cda.org.hl7.v3.adxp_street_name import AdxpStreetName
from cda.org.hl7.v3.adxp_street_name_base import AdxpStreetNameBase
from cda.org.hl7.v3.adxp_street_name_type import AdxpStreetNameType
from cda.org.hl7.v3.adxp_unit_id import AdxpUnitId
from cda.org.hl7.v3.adxp_unit_type import AdxpUnitType
from cda.org.hl7.v3.any import Any
from cda.org.hl7.v3.postal_address_use import PostalAddressUse
from cda.org.hl7.v3.sxcm_ts import SxcmTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Ad(Any):
    """Mailing and home or office addresses.

    A sequence of address parts, such as street or post office Box,
    city, postal code, country, etc.

    :ivar use: A set of codes advising a system or user which address in
        a set of like addresses to select for a given purpose.
    :ivar is_not_ordered: A boolean value specifying whether the order
        of the address parts is known or not. While the address parts
        are always a Sequence, the order in which they are presented may
        or may not be known. Where this matters, can be used to convey
        this information.
    :ivar content:
    """
    class Meta:
        name = "AD"

    use: List[PostalAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    is_not_ordered: Optional[str] = field(
        default=None,
        metadata={
            "name": "isNotOrdered",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "delimiter",
                    "type": AdxpDelimiter,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "country",
                    "type": AdxpCountry,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "state",
                    "type": AdxpState,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "county",
                    "type": AdxpCounty,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "city",
                    "type": AdxpCity,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "postalCode",
                    "type": AdxpPostalCode,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "streetAddressLine",
                    "type": AdxpStreetAddressLine,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "houseNumber",
                    "type": AdxpHouseNumber,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "houseNumberNumeric",
                    "type": AdxpHouseNumberNumeric,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "direction",
                    "type": AdxpDirection,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "streetName",
                    "type": AdxpStreetName,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "streetNameBase",
                    "type": AdxpStreetNameBase,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "streetNameType",
                    "type": AdxpStreetNameType,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "additionalLocator",
                    "type": AdxpAdditionalLocator,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "unitID",
                    "type": AdxpUnitId,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "unitType",
                    "type": AdxpUnitType,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "careOf",
                    "type": AdxpCareOf,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "censusTract",
                    "type": AdxpCensusTract,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryAddressLine",
                    "type": AdxpDeliveryAddressLine,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryInstallationType",
                    "type": AdxpDeliveryInstallationType,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryInstallationArea",
                    "type": AdxpDeliveryInstallationArea,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryInstallationQualifier",
                    "type": AdxpDeliveryInstallationQualifier,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryMode",
                    "type": AdxpDeliveryMode,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "deliveryModeIdentifier",
                    "type": AdxpDeliveryModeIdentifier,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "buildingNumberSuffix",
                    "type": AdxpBuildingNumberSuffix,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "postBox",
                    "type": AdxpPostBox,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "precinct",
                    "type": AdxpPrecinct,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "useablePeriod",
                    "type": SxcmTs,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        }
    )
