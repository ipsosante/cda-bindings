from dataclasses import dataclass, field
from typing import Any

from cdabindings.versioned_element_type import VersionedElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class TextElementBaseType(VersionedElementType):
    class Meta:
        name = "text-element-base-type"

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")
