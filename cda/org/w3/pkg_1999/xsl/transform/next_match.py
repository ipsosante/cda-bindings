from dataclasses import dataclass, field
from typing import List
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class NextMatch(ElementOnlyVersionedElementType):
    class Meta:
        name = "next-match"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    with_param: List["WithParam"] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        }
    )
    fallback: List["Fallback"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
