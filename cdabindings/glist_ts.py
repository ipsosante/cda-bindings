from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract
from cdabindings.pq import PQ
from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class GlistTs(AnyAbstract):
    """
    :ivar head: This is the start-value of the generated list.
    :ivar increment: The difference between one value and its previous
        different value. For example, to generate the sequence (1; 4; 7;
        10; 13; ...) the increment is 3; likewise to generate the
        sequence (1; 1; 4; 4; 7; 7; 10; 10; 13; 13; ...) the increment
        is also 3.
    :ivar period: If non-NULL, specifies that the sequence alternates,
        i.e., after this many increments, the sequence item values roll
        over to start from the initial sequence item value. For example,
        the sequence (1; 2; 3; 1; 2; 3; 1; 2; 3; ...) has period 3; also
        the sequence (1; 1; 2; 2; 3; 3; 1; 1; 2; 2; 3; 3; ...) has
        period 3 too.
    :ivar denominator: The integer by which the index for the sequence
        is divided, effectively the number of times the sequence
        generates the same sequence item value before incrementing to
        the next sequence item value. For example, to generate the
        sequence (1; 1; 1; 2; 2; 2; 3; 3; 3; ...)  the denominator is 3.
    """

    class Meta:
        name = "GLIST_TS"

    head: Optional[TS] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    increment: Optional[PQ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    denominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
