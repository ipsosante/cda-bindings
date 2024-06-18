from dataclasses import dataclass, field
from typing import Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.otherwise import Otherwise
from cdabindings.when import When

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Choose(ElementOnlyVersionedElementType):
    class Meta:
        name = "choose"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    when: list[When] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    otherwise: Optional[Otherwise] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
