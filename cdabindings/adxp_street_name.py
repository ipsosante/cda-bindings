from dataclasses import dataclass, field

from cdabindings.address_part_type import AddressPartType
from cdabindings.adxp import Adxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AdxpStreetName(Adxp):
    class Meta:
        name = "adxp.streetName"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.STR,
        metadata={
            "name": "partType",
            "type": "Attribute",
        },
    )
