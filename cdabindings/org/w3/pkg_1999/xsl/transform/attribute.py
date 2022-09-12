from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cdabindings.org.w3.pkg_1999.xsl.transform.validation_type import ValidationType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Attribute(SequenceConstructor):
    class Meta:
        name = "attribute"
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
    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    separator: Optional[str] = field(
        default=None,
        metadata={
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
