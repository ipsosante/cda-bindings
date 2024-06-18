from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.complex_type_abstract import Element1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelElement(Element1):
    class Meta:
        name = "topLevelElement"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    form: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    max_occurs: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
