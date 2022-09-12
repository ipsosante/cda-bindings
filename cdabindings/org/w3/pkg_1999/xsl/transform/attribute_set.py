from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.attribute import Attribute
from cdabindings.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class AttributeSet(ElementOnlyVersionedElementType):
    class Meta:
        name = "attribute-set"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
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
    use_attribute_sets: List[str] = field(
        default_factory=list,
        metadata={
            "name": "use-attribute-sets",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
            "tokens": True,
        }
    )
