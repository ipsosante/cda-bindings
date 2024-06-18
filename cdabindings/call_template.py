from dataclasses import dataclass, field
from typing import Optional

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.with_param import WithParam

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class CallTemplate(ElementOnlyVersionedElementType):
    class Meta:
        name = "call-template"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    with_param: list[WithParam] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
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
