from dataclasses import dataclass, field
from typing import Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.fallback import Fallback

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Sequence2(ElementOnlyVersionedElementType):
    class Meta:
        name = "sequence"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "fallback",
                    "type": Fallback,
                },
            ),
        },
    )
