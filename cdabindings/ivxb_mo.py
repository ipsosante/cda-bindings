from dataclasses import dataclass, field

from cdabindings.mo import Mo

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class IvxbMo(Mo):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_MO"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
