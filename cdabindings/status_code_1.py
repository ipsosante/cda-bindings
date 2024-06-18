from dataclasses import dataclass

from cdabindings.cs import CS

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class StatusCode1(CS):
    class Meta:
        name = "statusCode"
        namespace = "urn:hl7-org:sdtc"
