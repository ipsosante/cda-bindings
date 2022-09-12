from dataclasses import dataclass, field
from cdabindings.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvxbTs(TS):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """
    class Meta:
        name = "IVXB_TS"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
