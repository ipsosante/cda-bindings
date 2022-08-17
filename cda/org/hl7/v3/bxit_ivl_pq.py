from dataclasses import dataclass, field
from cda.org.hl7.v3.ivl_pq import IvlPq

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class BxitIvlPq(IvlPq):
    """
    :ivar qty: The quantity in which the bag item occurs in its
        containing bag.
    """
    class Meta:
        name = "BXIT_IVL_PQ"

    qty: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
