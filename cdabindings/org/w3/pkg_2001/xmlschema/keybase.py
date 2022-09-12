from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.w3.pkg_2001.xmlschema.annotated import Annotated
from cdabindings.org.w3.pkg_2001.xmlschema.field_mod import Field
from cdabindings.org.w3.pkg_2001.xmlschema.selector import Selector

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
        }
    )
    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "min_occurs": 1,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
