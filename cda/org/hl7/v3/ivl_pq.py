from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.ivxb_pq import IvxbPq
from cda.org.hl7.v3.pq import Pq
from cda.org.hl7.v3.sxcm_pq import SxcmPq

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvlPq(SxcmPq):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """
    class Meta:
        name = "IVL_PQ"

    low: Optional[IvxbPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    width: List[Pq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    high: List[IvxbPq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    center: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
