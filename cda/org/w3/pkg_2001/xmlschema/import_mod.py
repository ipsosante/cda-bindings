from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Import(Annotated):
    class Meta:
        name = "import"
        namespace = "http://www.w3.org/2001/XMLSchema"

    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaLocation",
            "type": "Attribute",
        }
    )
