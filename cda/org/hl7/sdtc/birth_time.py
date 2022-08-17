from dataclasses import dataclass
from cda.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class BirthTime(TS):
    class Meta:
        name = "birthTime"
        namespace = "urn:hl7-org:sdtc"
