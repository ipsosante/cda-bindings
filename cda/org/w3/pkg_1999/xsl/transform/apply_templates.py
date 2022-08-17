from dataclasses import dataclass, field
from typing import List, Optional, Union
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType
from cda.org.w3.pkg_1999.xsl.transform.mode_value import ModeValue

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ApplyTemplates(ElementOnlyVersionedElementType):
    class Meta:
        name = "apply-templates"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    sort: List["Sort"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    with_param: List["WithParam"] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        }
    )
    select: str = field(
        default="child::node()",
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    mode: Optional[Union[str, ModeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
