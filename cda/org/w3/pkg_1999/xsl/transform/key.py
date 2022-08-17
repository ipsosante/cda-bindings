from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Key(SequenceConstructor):
    class Meta:
        name = "key"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    match: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".+",
        }
    )
    use: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    collation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
