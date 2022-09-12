from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Message(SequenceConstructor):
    class Meta:
        name = "message"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    terminate: str = field(
        default="no",
        metadata={
            "type": "Attribute",
        }
    )
