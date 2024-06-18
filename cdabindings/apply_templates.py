from dataclasses import dataclass, field
from typing import Optional, Union

from cdabindings.element_only_versioned_element_type import (
    ElementOnlyVersionedElementType,
)
from cdabindings.mode_value import ModeValue
from cdabindings.sort import Sort
from cdabindings.with_param import WithParam

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class ApplyTemplates(ElementOnlyVersionedElementType):
    class Meta:
        name = "apply-templates"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    sort: list[Sort] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    with_param: list[WithParam] = field(
        default_factory=list,
        metadata={
            "name": "with-param",
            "type": "Element",
        },
    )
    select: str = field(
        default="child::node()",
        metadata={
            "type": "Attribute",
            "pattern": r".+",
        },
    )
    mode: Optional[Union[str, ModeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"([^:]+:)?[^:]+",
        },
    )
