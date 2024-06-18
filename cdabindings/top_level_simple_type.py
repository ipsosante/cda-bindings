from dataclasses import dataclass, field
from typing import Any, Optional

from cdabindings.simple_type_abstract import SimpleTypeAbstract

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelSimpleType(SimpleTypeAbstract):
    """
    :ivar any_element:
    :ivar name: Required at the top level
    """

    class Meta:
        name = "topLevelSimpleType"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
