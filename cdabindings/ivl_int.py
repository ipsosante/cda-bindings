from dataclasses import dataclass, field
from typing import Optional

from cdabindings.int_mod import Int
from cdabindings.ivxb_int import IvxbInt
from cdabindings.sxcm_int import SxcmInt

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvlInt(SxcmInt):
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
        name = "IVL_INT"

    low: Optional[IvxbInt] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbInt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
