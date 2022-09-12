from dataclasses import dataclass, field
from cdabindings.org.hl7.v3.ppd_ts import PpdTs
from cdabindings.org.hl7.v3.set_operator import SetOperator

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SxcmPpdTs(PpdTs):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """
    class Meta:
        name = "SXCM_PPD_TS"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        }
    )
