from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ivl_ts import IvlTs
from cdabindings.pq import Pq

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class HxitPq(Pq):
    """
    :ivar valid_time: The time interval during which the given
        information was, is, or is expected to be valid. The interval
        can be open or closed, as well as infinite or undefined on
        either side.
    """

    class Meta:
        name = "HXIT_PQ"

    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
