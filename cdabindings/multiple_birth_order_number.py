from dataclasses import dataclass

from cdabindings.int_pos import IntPos

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class MultipleBirthOrderNumber(IntPos):
    class Meta:
        name = "multipleBirthOrderNumber"
        namespace = "urn:hl7-org:sdtc"
