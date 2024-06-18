from dataclasses import dataclass

from cdabindings.int_mod import Int

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class PriorityNumber(Int):
    class Meta:
        name = "priorityNumber"
        namespace = "urn:hl7-org:sdtc"
