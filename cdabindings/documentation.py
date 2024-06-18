from dataclasses import dataclass, field
from typing import Optional, Union

from cdabindings.lang_value import LangValue

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Documentation:
    class Meta:
        name = "documentation"
        namespace = "http://www.w3.org/2001/XMLSchema"

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
