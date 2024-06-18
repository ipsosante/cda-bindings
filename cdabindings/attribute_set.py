from dataclasses import dataclass, field
from typing import Optional

from cdabindings.attribute_3 import Attribute3
from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class AttributeSet(ElementOnlyVersionedElementType):
    class Meta:
        name = "attribute-set"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    attribute: list[Attribute3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
        },
    )
    use_attribute_sets: list[str] = field(
        default_factory=list,
        metadata={
            "name": "use-attribute-sets",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
            "tokens": True,
        },
    )
