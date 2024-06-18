from dataclasses import dataclass, field
from typing import Optional

from cdabindings.level import Level
from cdabindings.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Number(VersionedElementType):
    class Meta:
        name = "number"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    level: Level = field(
        default=Level.SINGLE,
        metadata={
            "type": "Attribute",
        },
    )
    count: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    format: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    letter_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "letter-value",
            "type": "Attribute",
        },
    )
    ordinal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    grouping_separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "grouping-separator",
            "type": "Attribute",
        },
    )
    grouping_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "grouping-size",
            "type": "Attribute",
        },
    )
