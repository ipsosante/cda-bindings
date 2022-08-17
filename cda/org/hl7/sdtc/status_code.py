from dataclasses import dataclass
from cda.org.hl7.v3.cs import CS

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class StatusCode(CS):
    class Meta:
        name = "statusCode"
        namespace = "urn:hl7-org:sdtc"
