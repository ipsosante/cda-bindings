from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.w3.pkg_2001.xmlschema.appinfo import Appinfo
from cda.org.w3.pkg_2001.xmlschema.documentation import Documentation
from cda.org.w3.pkg_2001.xmlschema.open_attrs import OpenAttrs

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Annotation(OpenAttrs):
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    appinfo: List[Appinfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    documentation: List[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
