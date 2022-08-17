from dataclasses import dataclass
from cda.org.hl7.v3.ed import ED

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Desc(ED):
    class Meta:
        name = "desc"
        namespace = "urn:hl7-org:sdtc"
