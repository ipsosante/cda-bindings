from dataclasses import dataclass, field
from typing import Any

from cdabindings.complex_type_abstract import ExplicitGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleExplicitGroup(ExplicitGroup):
    class Meta:
        name = "simpleExplicitGroup"

    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
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
