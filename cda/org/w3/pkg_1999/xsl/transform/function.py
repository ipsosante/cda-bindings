from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType
from cda.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Function(VersionedElementType):
    class Meta:
        name = "function"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    override: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "type": "Attribute",
        }
    )
    as_value: str = field(
        default="item()*",
        metadata={
            "name": "as",
            "type": "Attribute",
            "pattern": r".+",
        }
    )
