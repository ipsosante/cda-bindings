from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class OpenAttrs:
    """
    This type is extended by almost all schema types to allow attributes from other
    namespaces to be added to user schemas.
    """

    class Meta:
        name = "openAttrs"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
