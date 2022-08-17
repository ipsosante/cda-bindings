from dataclasses import dataclass, field
from cda.org.hl7.v3.real import Real

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvxbReal(Real):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """
    class Meta:
        name = "IVXB_REAL"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
