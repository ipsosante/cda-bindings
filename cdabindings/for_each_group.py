from dataclasses import dataclass, field
from typing import Optional

from cdabindings.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ForEachGroup(VersionedElementType):
    class Meta:
        name = "for-each-group"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        },
    )
    group_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "group-by",
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    group_adjacent: Optional[str] = field(
        default=None,
        metadata={
            "name": "group-adjacent",
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    group_starting_with: Optional[str] = field(
        default=None,
        metadata={
            "name": "group-starting-with",
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    group_ending_with: Optional[str] = field(
        default=None,
        metadata={
            "name": "group-ending-with",
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    collation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
