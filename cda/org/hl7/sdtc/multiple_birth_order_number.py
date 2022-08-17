from dataclasses import dataclass
from cda.org.hl7.sdtc.int_pos import IntPos

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class MultipleBirthOrderNumber(IntPos):
    class Meta:
        name = "multipleBirthOrderNumber"
        namespace = "urn:hl7-org:sdtc"
