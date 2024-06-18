from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.complex_type_abstract import (
    All,
    RealGroup,
)
from cdabindings.simple_explicit_group import SimpleExplicitGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NamedGroup(RealGroup):
    class Meta:
        name = "namedGroup"

    element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
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
    all: list["NamedGroup.All"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: list[SimpleExplicitGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: list[SimpleExplicitGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref: Any = field(
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

    @dataclass
    class All(All):
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
        group: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        choice: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        sequence: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        any: Any = field(
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
