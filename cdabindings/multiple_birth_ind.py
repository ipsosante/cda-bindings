from dataclasses import dataclass

from cdabindings.bl import Bl

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class MultipleBirthInd(Bl):
    class Meta:
        name = "multipleBirthInd"
        namespace = "urn:hl7-org:sdtc"
