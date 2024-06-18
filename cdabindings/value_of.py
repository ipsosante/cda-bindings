from dataclasses import dataclass, field
from typing import Optional

from cdabindings.sequence_constructor import SequenceConstructor
from cdabindings.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ValueOf(SequenceConstructor):
    class Meta:
        name = "value-of"
        namespace = "http://www.w3.org/1999/XSL/Transform"

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
    disable_output_escaping: YesOrNo = field(
        default=YesOrNo.NO,
        metadata={
            "name": "disable-output-escaping",
            "type": "Attribute",
        },
    )
