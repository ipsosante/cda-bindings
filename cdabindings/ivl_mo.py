from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ivxb_mo import IvxbMo
from cdabindings.mo import Mo
from cdabindings.sxcm_mo import SxcmMo

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvlMo(SxcmMo):
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
        name = "IVL_MO"

    low: Optional[IvxbMo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Mo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbMo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Mo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
