from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.address_part_type import AddressPartType
from cdabindings.org.hl7.v3.st import ST

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Adxp(ST):
    """A character string that may have a type-tag signifying its role in the
    address.

    Typical parts that exist in about every address are street, house
    number, or post box, postal code, city, country but other roles may
    be defined regionally, nationally, or on an enterprise level (e.g.
    in military addresses). Addresses are usually broken up into lines,
    which are indicated by special line-breaking delimiter elements
    (e.g., DEL).

    :ivar part_type: Specifies whether an address part names the street,
        city, country, postal code, post box, etc. If the type is NULL
        the address part is unclassified and would simply appear on an
        address label as is.
    """
    class Meta:
        name = "ADXP"

    part_type: Optional[AddressPartType] = field(
        default=None,
        metadata={
            "name": "partType",
            "type": "Attribute",
        }
    )
