from dataclasses import dataclass
from cdabindings.org.hl7.v3.en import En

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Tn(En):
    """
    A restriction of entity name that is effectively a simple string used for a
    simple name for things and places.
    """
    class Meta:
        name = "TN"
