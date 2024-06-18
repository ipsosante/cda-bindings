from dataclasses import dataclass, field
from typing import Optional

from cdabindings.appinfo import Appinfo
from cdabindings.documentation import Documentation
from cdabindings.open_attrs import OpenAttrs

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Annotation(OpenAttrs):
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    appinfo: list[Appinfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    documentation: list[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
