from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.any import Any

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Bl(Any):
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
        }
    )
