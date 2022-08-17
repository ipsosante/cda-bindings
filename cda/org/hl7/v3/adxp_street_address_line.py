from dataclasses import dataclass, field
from cda.org.hl7.v3.address_part_type import AddressPartType
from cda.org.hl7.v3.adxp import Adxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AdxpStreetAddressLine(Adxp):
    class Meta:
        name = "adxp.streetAddressLine"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.SAL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
