from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.attribute_1 import Attribute1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelAttribute(Attribute1):
    class Meta:
        name = "topLevelAttribute"

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
    use: Any = field(
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
