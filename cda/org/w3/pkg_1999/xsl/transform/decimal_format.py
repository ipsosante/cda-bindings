from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class DecimalFormat(ElementOnlyVersionedElementType):
    class Meta:
        name = "decimal-format"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    decimal_separator: str = field(
        default=".",
        metadata={
            "name": "decimal-separator",
            "type": "Attribute",
            "length": 1,
        }
    )
    grouping_separator: str = field(
        default=",",
        metadata={
            "name": "grouping-separator",
            "type": "Attribute",
            "length": 1,
        }
    )
    infinity: str = field(
        default="Infinity",
        metadata={
            "type": "Attribute",
        }
    )
    minus_sign: str = field(
        default="-",
        metadata={
            "name": "minus-sign",
            "type": "Attribute",
            "length": 1,
        }
    )
    na_n: str = field(
        default="NaN",
        metadata={
            "name": "NaN",
            "type": "Attribute",
        }
    )
    percent: str = field(
        default="%",
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    per_mille: str = field(
        default="‰",
        metadata={
            "name": "per-mille",
            "type": "Attribute",
            "length": 1,
        }
    )
    zero_digit: str = field(
        default="0",
        metadata={
            "name": "zero-digit",
            "type": "Attribute",
            "length": 1,
        }
    )
    digit: str = field(
        default="#",
        metadata={
            "type": "Attribute",
            "length": 1,
        }
    )
    pattern_separator: str = field(
        default=";",
        metadata={
            "name": "pattern-separator",
            "type": "Attribute",
            "length": 1,
        }
    )
