from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Include(ElementOnlyVersionedElementType):
    class Meta:
        name = "include"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
