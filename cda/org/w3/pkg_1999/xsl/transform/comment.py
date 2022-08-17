from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Comment(SequenceConstructor):
    class Meta:
        name = "comment"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    select: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
