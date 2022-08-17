from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_1999.xsl.transform.sequence_constructor import SequenceConstructor
from cda.org.w3.pkg_1999.xsl.transform.validation_type import ValidationType

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Document(SequenceConstructor):
    class Meta:
        name = "document"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        }
    )
    validation: Optional[ValidationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
