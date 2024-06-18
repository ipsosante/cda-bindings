from dataclasses import dataclass, field
from typing import Optional

from cdabindings.sequence_constructor import SequenceConstructor
from cdabindings.validation_type import ValidationType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Attribute3(SequenceConstructor):
    class Meta:
        name = "attribute"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    separator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        },
    )
    validation: Optional[ValidationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
