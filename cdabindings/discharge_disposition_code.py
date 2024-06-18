from dataclasses import dataclass

from cdabindings.ce import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class DischargeDispositionCode(CE):
    class Meta:
        name = "dischargeDispositionCode"
        namespace = "urn:hl7-org:sdtc"
