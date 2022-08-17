from dataclasses import dataclass, field
from cda.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class TextElementBaseType(VersionedElementType):
    class Meta:
        name = "text-element-base-type"

    value: str = field(
        default=""
    )
