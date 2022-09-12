from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Sort(SequenceConstructor):
    class Meta:
        name = "sort"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    data_type: str = field(
        default="text",
        metadata={
            "name": "data-type",
            "type": "Attribute",
        }
    )
    order: str = field(
        default="ascending",
        metadata={
            "type": "Attribute",
        }
    )
    case_order: Optional[str] = field(
        default=None,
        metadata={
            "name": "case-order",
            "type": "Attribute",
        }
    )
    collation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stable: Optional[YesOrNo] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
