from dataclasses import dataclass

from cdabindings.bl import BL

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class MultipleBirthInd(BL):
    class Meta:
        name = "multipleBirthInd"
        namespace = "urn:hl7-org:sdtc"
