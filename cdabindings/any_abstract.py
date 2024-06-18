from dataclasses import dataclass, field
from typing import Optional

from cdabindings.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AnyAbstract:
    """Defines the basic properties of every data value.

    This is an abstract type, meaning that no value can be just a data
    value without belonging to any concrete type. Every concrete type is
    a specialization of this general abstract DataValue type.

    :ivar null_flavor: An exceptional value expressing missing
        information and possibly the reason why the information is
        missing.
    """

    class Meta:
        name = "ANY"

    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
