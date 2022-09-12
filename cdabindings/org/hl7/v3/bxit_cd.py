from dataclasses import dataclass, field
from cdabindings.org.hl7.v3.cr import CD

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class BxitCd(CD):
    """
    :ivar qty: The quantity in which the bag item occurs in its
        containing bag.
    """
    class Meta:
        name = "BXIT_CD"

    qty: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
