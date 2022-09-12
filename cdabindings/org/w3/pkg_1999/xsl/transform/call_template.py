from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class CallTemplate(ElementOnlyVersionedElementType):
    class Meta:
        name = "call-template"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    with_param: List["WithParam"] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
