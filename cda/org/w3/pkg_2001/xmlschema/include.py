from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Include(Annotated):
    class Meta:
        name = "include"
        namespace = "http://www.w3.org/2001/XMLSchema"

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
            "required": True,
        }
    )
