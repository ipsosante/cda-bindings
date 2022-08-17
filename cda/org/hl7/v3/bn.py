from dataclasses import dataclass, field
from typing import Optional
from cda.org.hl7.v3.anynon_null import AnynonNull

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Bn(AnynonNull):
    """The BooleanNonNull type is used where a Boolean cannot have a null
    value.

    A Boolean value can be either true or false.
    """
    class Meta:
        name = "BN"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
