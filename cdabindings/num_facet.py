from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.facet import Facet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NumFacet(Facet):
    class Meta:
        name = "numFacet"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
