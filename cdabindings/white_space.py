from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.facet import Facet
from cdabindings.white_space_value import WhiteSpaceValue

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class WhiteSpace(Facet):
    class Meta:
        name = "whiteSpace"
        namespace = "http://www.w3.org/2001/XMLSchema"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[WhiteSpaceValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
