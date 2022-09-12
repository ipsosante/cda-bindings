from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cdabindings.org.w3.pkg_1999.xsl.transform.validation_type import ValidationType
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Element(SequenceConstructor):
    class Meta:
        name = "element"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inherit_namespaces: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "name": "inherit-namespaces",
            "type": "Attribute",
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
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    validation: Optional[ValidationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
