from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class TransformElementBaseType(ElementOnlyVersionedElementType):
    class Meta:
        name = "transform-element-base-type"

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
