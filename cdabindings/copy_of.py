from dataclasses import dataclass, field
from typing import Optional

from cdabindings.validation_type import ValidationType
from cdabindings.versioned_element_type import VersionedElementType
from cdabindings.yes_or_no import YesOrNo

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
        },
    )
    copy_namespaces: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "name": "copy-namespaces",
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        },
    )
    validation: Optional[ValidationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
