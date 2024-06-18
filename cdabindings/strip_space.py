from dataclasses import dataclass, field

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.nametests_value import NametestsValue

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class StripSpace(ElementOnlyVersionedElementType):
    class Meta:
        name = "strip-space"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    elements: list[NametestsValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
