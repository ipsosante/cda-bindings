from dataclasses import dataclass
from cda.org.hl7.v3.cr import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class RaceCode(CE):
    class Meta:
        name = "raceCode"
        namespace = "urn:hl7-org:sdtc"
