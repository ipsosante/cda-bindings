from dataclasses import dataclass
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class TransformElementBaseType(ElementOnlyVersionedElementType):
    class Meta:
        name = "transform-element-base-type"
