from dataclasses import dataclass, field
from typing import Optional
from cda.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Int(Qty):
    """Integer numbers (-1,0,1,2, 100, 3398129, etc.) are precise numbers that
    are results of counting and enumerating.

    Integer numbers are discrete, the set of integers is infinite but
    countable.  No arbitrary limit is imposed on the range of integer
    numbers. Two NULL flavors are defined for the positive and negative
    infinity.
    """
    class Meta:
        name = "INT"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
