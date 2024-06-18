from dataclasses import dataclass, field
from typing import Optional

from cdabindings.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class When(SequenceConstructor):
    class Meta:
        name = "when"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    test: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        },
    )
