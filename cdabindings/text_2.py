from dataclasses import dataclass

from cdabindings.ed import ED

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Text2(ED):
    class Meta:
        name = "text"
        namespace = "urn:hl7-org:sdtc"
