from dataclasses import dataclass, field

from cdabindings.ppd_pq import PpdPq
from cdabindings.set_operator import SetOperator

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SxcmPpdPq(PpdPq):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_PPD_PQ"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )
