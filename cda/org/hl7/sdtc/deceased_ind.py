from dataclasses import dataclass
from cda.org.hl7.v3.bl import Bl

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class DeceasedInd(Bl):
    class Meta:
        name = "deceasedInd"
        namespace = "urn:hl7-org:sdtc"
