from dataclasses import dataclass, field
from typing import Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Import2(ElementOnlyVersionedElementType):
    class Meta:
        name = "import"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
