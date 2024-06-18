from dataclasses import dataclass

from cdabindings.ed import ED

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Desc1(ED):
    class Meta:
        name = "desc"
        namespace = "urn:hl7-org:sdtc"
