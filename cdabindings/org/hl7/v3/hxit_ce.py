from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.ivl_ts import IvlTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class HxitCe(CE):
    """
    :ivar valid_time: The time interval during which the given
        information was, is, or is expected to be valid. The interval
        can be open or closed, as well as infinite or undefined on
        either side.
    """
    class Meta:
        name = "HXIT_CE"

    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
