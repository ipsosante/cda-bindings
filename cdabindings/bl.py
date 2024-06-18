from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Bl(AnyAbstract):
    """The Boolean type stands for the values of two-valued logic.

    A Boolean value can be either true or false, or, as any other value
    may be NULL.
    """

    class Meta:
        name = "BL"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
