from dataclasses import dataclass, field
from typing import Optional

from cdabindings.annotated import Annotated
from cdabindings.field_mod import FieldType
from cdabindings.selector import Selector

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Keybase(Annotated):
    class Meta:
        name = "keybase"

    selector: Optional[Selector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "required": True,
        },
    )
    field_value: list[FieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "min_occurs": 1,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
