from dataclasses import dataclass, field
from typing import Dict, List, Optional

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Appinfo:
    class Meta:
        name = "appinfo"
        namespace = "http://www.w3.org/2001/XMLSchema"

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
