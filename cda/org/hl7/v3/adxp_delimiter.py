from dataclasses import dataclass, field
from cda.org.hl7.v3.address_part_type import AddressPartType
from cda.org.hl7.v3.adxp import Adxp

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AdxpDelimiter(Adxp):
    class Meta:
        name = "adxp.delimiter"

    part_type: AddressPartType = field(
        init=False,
        default=AddressPartType.DEL,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
