from dataclasses import dataclass, field
from typing import Any

from cdabindings.any_abstract import AnyAbstract
from cdabindings.null_flavor import NullFlavor

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AnynonNull(AnyAbstract):
    """The BooleanNonNull type is used where a Boolean cannot have a null value.

    A Boolean value can be either true or false.
    """

    class Meta:
        name = "ANYNonNull"

    null_flavor: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
