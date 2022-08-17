from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Choose(ElementOnlyVersionedElementType):
    class Meta:
        name = "choose"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    when: List["When"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    otherwise: Optional["Otherwise"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
