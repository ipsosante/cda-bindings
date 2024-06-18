from dataclasses import dataclass, field
from typing import Any

from cdabindings.facet import Facet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NoFixedFacet(Facet):
    class Meta:
        name = "noFixedFacet"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    fixed: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
