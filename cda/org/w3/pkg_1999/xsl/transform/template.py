from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.modes import Modes
from cda.org.w3.pkg_1999.xsl.transform.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Template(VersionedElementType):
    class Meta:
        name = "template"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    match: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    priority: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mode: Optional[Modes] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
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
