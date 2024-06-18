from dataclasses import dataclass, field
from typing import Optional

from cdabindings.sequence_constructor import SequenceConstructor
from cdabindings.validation_type import ValidationType
from cdabindings.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Copy(SequenceConstructor):
    class Meta:
        name = "copy"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    copy_namespaces: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "name": "copy-namespaces",
            "type": "Attribute",
        },
    )
    inherit_namespaces: YesOrNo = field(
        default=YesOrNo.YES,
        metadata={
            "name": "inherit-namespaces",
            "type": "Attribute",
        },
    )
    use_attribute_sets: list[str] = field(
        default_factory=list,
        metadata={
            "name": "use-attribute-sets",
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
            "tokens": True,
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
