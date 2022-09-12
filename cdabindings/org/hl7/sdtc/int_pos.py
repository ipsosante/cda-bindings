from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class IntPos(Qty):
    """
    Positive integer numbers.
    """
    class Meta:
        name = "INT_POS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
