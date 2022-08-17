from dataclasses import dataclass, field
from typing import List
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType
from cda.org.w3.pkg_1999.xsl.transform.nametests_value import NametestsValue

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class StripSpace(ElementOnlyVersionedElementType):
    class Meta:
        name = "strip-space"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    elements: List[NametestsValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )
