from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from cdabindings.generic_element_type import GenericElementType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class VersionedElementType(GenericElementType):
    class Meta:
        name = "versioned-element-type"

    version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
