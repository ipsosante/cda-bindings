from dataclasses import dataclass, field
from typing import Optional

from cdabindings.mo import Mo
from cdabindings.pq import PQ
from cdabindings.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RtoMoPq(Qty):
    """
    :ivar numerator: The quantity that is being divided in the ratio.
        The default is the integer number 1 (one).
    :ivar denominator: The quantity that devides the numerator in the
        ratio. The default is the integer number 1 (one). The
        denominator must not be zero.
    """

    class Meta:
        name = "RTO_MO_PQ"

    numerator: Optional[Mo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    denominator: Optional[PQ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
