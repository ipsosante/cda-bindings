from dataclasses import dataclass, field
from typing import Optional

from cdabindings.sequence_constructor import SequenceConstructor
from cdabindings.validation_type import ValidationType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Document(SequenceConstructor):
    class Meta:
        name = "document"
        namespace = "http://www.w3.org/1999/XSL/Transform"

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
