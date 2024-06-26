from dataclasses import dataclass

from cdabindings.ed import ED

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class SignatureText(ED):
    class Meta:
        name = "signatureText"
        namespace = "urn:hl7-org:sdtc"
