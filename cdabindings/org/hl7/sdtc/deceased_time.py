from dataclasses import dataclass
from cdabindings.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class DeceasedTime(TS):
    class Meta:
        name = "deceasedTime"
        namespace = "urn:hl7-org:sdtc"
