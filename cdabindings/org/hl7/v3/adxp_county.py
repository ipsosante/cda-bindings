from dataclasses import dataclass, field
from cdabindings.org.hl7.v3.address_part_type import AddressPartType
from cdabindings.org.hl7.v3.adxp import Adxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AdxpCounty(Adxp):
    class Meta:
        name = "adxp.county"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.CPA,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
