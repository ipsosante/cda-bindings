from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.w3.pkg_2001.xmlschema.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Facet(Annotated):
    class Meta:
        name = "facet"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
