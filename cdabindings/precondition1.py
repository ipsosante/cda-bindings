from dataclasses import dataclass

from cdabindings.precondition1_1 import Precondition11

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Precondition1(Precondition11):
    class Meta:
        name = "precondition1"
        namespace = "urn:hl7-org:sdtc"
