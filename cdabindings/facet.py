from dataclasses import dataclass, field
from typing import Optional

from cdabindings.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Facet(Annotated):
    class Meta:
        name = "facet"

    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    fixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
