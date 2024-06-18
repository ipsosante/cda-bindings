from dataclasses import dataclass, field
from typing import Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class OutputCharacter(ElementOnlyVersionedElementType):
    class Meta:
        name = "output-character"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    character: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "length": 1,
        },
    )
    string: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
