from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract
from cdabindings.pq import PQ
from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SlistTs(AnyAbstract):
    """
    :ivar origin: The origin of the list item value scale, i.e., the
        physical quantity that a zero-digit in the sequence would
        represent.
    :ivar scale: A ratio-scale quantity that is factored out of the
        digit sequence.
    :ivar digits: A sequence of raw digits for the sample values. This
        is typically the raw output of an A/D converter.
    """

    class Meta:
        name = "SLIST_TS"

    origin: Optional[TS] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    scale: Optional[PQ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    digits: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "tokens": True,
        },
    )
