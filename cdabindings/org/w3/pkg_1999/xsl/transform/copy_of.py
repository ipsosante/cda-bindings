from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.validation_type import ValidationType
from cdabindings.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class CopyOf(VersionedElementType):
    class Meta:
        name = "copy-of"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        }
    )
    copy_namespaces: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "name": "copy-namespaces",
            "type": "Attribute",
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
