from dataclasses import dataclass

from cdabindings.bl import BL

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class DeceasedInd(BL):
    class Meta:
        name = "deceasedInd"
        namespace = "urn:hl7-org:sdtc"
