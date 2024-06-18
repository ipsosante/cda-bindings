from dataclasses import dataclass

from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class BirthTime(TS):
    class Meta:
        name = "birthTime"
        namespace = "urn:hl7-org:sdtc"
