from dataclasses import dataclass, field
from typing import Optional

from cdabindings.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ForEach(VersionedElementType):
    class Meta:
        name = "for-each"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        },
    )
