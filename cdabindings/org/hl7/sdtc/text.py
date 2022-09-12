from dataclasses import dataclass
from cdabindings.org.hl7.v3.ed import ED

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Text(ED):
    class Meta:
        name = "text"
        namespace = "urn:hl7-org:sdtc"
