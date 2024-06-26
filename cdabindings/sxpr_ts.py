from dataclasses import dataclass, field

from cdabindings.sxcm_ts import SxcmTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class SxprTs(SxcmTs):
    class Meta:
        name = "SXPR_TS"

    comp: list[SxcmTs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 2,
        },
    )
