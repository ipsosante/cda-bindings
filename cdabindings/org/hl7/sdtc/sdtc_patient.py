from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.ii import II

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class SdtcPatient:
    id: Optional[II] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
            "required": True,
        }
    )
