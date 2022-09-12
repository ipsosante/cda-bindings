from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_2001.xmlschema.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Notation(Annotated):
    class Meta:
        name = "notation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    public: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
