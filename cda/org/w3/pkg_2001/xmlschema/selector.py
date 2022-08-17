from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Selector(Annotated):
    class Meta:
        name = "selector"
        namespace = "http://www.w3.org/2001/XMLSchema"

    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"(\.//)?(((child::)?((\i\c*:)?(\i\c*|\*)))|\.)(/(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*(\|(\.//)?(((child::)?((\i\c*:)?(\i\c*|\*)))|\.)(/(((child::)?((\i\c*:)?(\i\c*|\*)))|\.))*)*",
        }
    )
