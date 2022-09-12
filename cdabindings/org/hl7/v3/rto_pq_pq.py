from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.pq import Pq
from cdabindings.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RtoPqPq(Qty):
    """
    :ivar numerator: The quantity that is being divided in the ratio.
        The default is the integer number 1 (one).
    :ivar denominator: The quantity that devides the numerator in the
        ratio. The default is the integer number 1 (one). The
        denominator must not be zero.
    """
    class Meta:
        name = "RTO_PQ_PQ"

    numerator: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    denominator: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
