from dataclasses import dataclass
from cdabindings.org.hl7.v3.any import Any

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class AnynonNull(Any):
    """The BooleanNonNull type is used where a Boolean cannot have a null
    value.

    A Boolean value can be either true or false.
    """
    class Meta:
        name = "ANYNonNull"
