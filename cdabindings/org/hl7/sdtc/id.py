from dataclasses import dataclass
from cdabindings.org.hl7.v3.ii import II

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Id(II):
    class Meta:
        name = "id"
        namespace = "urn:hl7-org:sdtc"
