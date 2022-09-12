from dataclasses import dataclass
from cdabindings.org.hl7.v3.en import En

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class On(En):
    """A name for an organization.

    A sequence of name parts.
    """
    class Meta:
        name = "ON"
