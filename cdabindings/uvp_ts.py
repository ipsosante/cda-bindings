from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class UvpTs(TS):
    """
    :ivar probability: The probability assigned to the value, a decimal
        number between 0 (very uncertain) and 1 (certain).
    """

    class Meta:
        name = "UVP_TS"

    probability: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
