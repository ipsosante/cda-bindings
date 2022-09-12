from dataclasses import dataclass
from cdabindings.org.hl7.v3.cr import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class EthnicGroupCode(CE):
    class Meta:
        name = "ethnicGroupCode"
        namespace = "urn:hl7-org:sdtc"
