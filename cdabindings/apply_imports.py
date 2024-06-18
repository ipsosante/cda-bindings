from dataclasses import dataclass, field

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.with_param import WithParam

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ApplyImports(ElementOnlyVersionedElementType):
    class Meta:
        name = "apply-imports"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    with_param: list[WithParam] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        },
    )
