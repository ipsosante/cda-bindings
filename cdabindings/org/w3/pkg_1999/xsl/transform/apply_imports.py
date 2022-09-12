from dataclasses import dataclass, field
from typing import List
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ApplyImports(ElementOnlyVersionedElementType):
    class Meta:
        name = "apply-imports"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    with_param: List["WithParam"] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        }
    )
