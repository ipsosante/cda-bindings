from dataclasses import dataclass, field

from cdabindings.address_part_type import AddressPartType
from cdabindings.adxp import Adxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AdxpCensusTract(Adxp):
    class Meta:
        name = "adxp.censusTract"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CEN,
        metadata={
            "name": "partType",
            "type": "Attribute",
        },
    )
