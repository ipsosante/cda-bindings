from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.no_fixed_facet import NoFixedFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Pattern(NoFixedFacet):
    class Meta:
        name = "pattern"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
