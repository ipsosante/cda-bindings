from dataclasses import dataclass, field

from cdabindings.ppd_pq import PpdPq

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvxbPpdPq(PpdPq):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_PPD_PQ"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
