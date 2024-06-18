from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.complex_type_abstract import ComplexTypeAbstract

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelComplexType(ComplexTypeAbstract):
    class Meta:
        name = "topLevelComplexType"

    any_element: Any = field(
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
