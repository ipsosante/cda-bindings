from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.v3.any import Any
from cdabindings.org.hl7.v3.pq import Pq
from cdabindings.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SlistTs(Any):
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
        }
    )
    scale: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    digits: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "tokens": True,
        }
    )
