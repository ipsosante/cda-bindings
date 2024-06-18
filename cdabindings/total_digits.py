from dataclasses import dataclass, field
from typing import Any

from cdabindings.num_facet import NumFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TotalDigits(NumFacet):
    class Meta:
        name = "totalDigits"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
