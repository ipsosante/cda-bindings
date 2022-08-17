from dataclasses import dataclass, field
from typing import Dict, List

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AnyType:
    """
    Not the real urType, but as close an approximation as we can get in the XML
    representation.
    """
    class Meta:
        name = "anyType"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
