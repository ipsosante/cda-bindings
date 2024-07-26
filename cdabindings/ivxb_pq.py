from dataclasses import dataclass, field

from cdabindings.pq import PQ

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvxbPq(PQ):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_PQ"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
