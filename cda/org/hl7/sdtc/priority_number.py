from dataclasses import dataclass
from cda.org.hl7.v3.int_mod import Int

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class PriorityNumber(Int):
    class Meta:
        name = "priorityNumber"
        namespace = "urn:hl7-org:sdtc"
