from dataclasses import dataclass, field
from typing import Optional

from cdabindings.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Include1(Annotated):
    class Meta:
        name = "include"
        namespace = "http://www.w3.org/2001/XMLSchema"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        },
    )
