from dataclasses import dataclass

from cdabindings.ce import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class RaceCode(CE):
    class Meta:
        name = "raceCode"
        namespace = "urn:hl7-org:sdtc"
