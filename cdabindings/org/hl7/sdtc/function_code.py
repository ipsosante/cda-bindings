from dataclasses import dataclass
from cdabindings.org.hl7.v3.cr import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class FunctionCode(CE):
    class Meta:
        name = "functionCode"
        namespace = "urn:hl7-org:sdtc"
