from dataclasses import dataclass

from cdabindings.ce import CE

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class EthnicGroupCode(CE):
    class Meta:
        name = "ethnicGroupCode"
        namespace = "urn:hl7-org:sdtc"
