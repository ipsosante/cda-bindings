from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class WithParam(SequenceConstructor):
    class Meta:
        name = "with-param"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    as_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "as",
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    tunnel: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
