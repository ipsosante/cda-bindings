from dataclasses import dataclass

from cdabindings.ii import II

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Id1(II):
    class Meta:
        name = "id"
        namespace = "urn:hl7-org:sdtc"
