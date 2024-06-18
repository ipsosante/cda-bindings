from dataclasses import dataclass, field
from typing import Optional

from cdabindings.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Import1(Annotated):
    class Meta:
        name = "import"
        namespace = "http://www.w3.org/2001/XMLSchema"

    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
        },
    )
